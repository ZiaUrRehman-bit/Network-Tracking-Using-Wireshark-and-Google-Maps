import dpkt  # Import the dpkt library for parsing and handling packet capture data (PCAP).
import socket  # Import the socket library for low-level networking interface.
import pygeoip  # Import the pygeoip library for IP address geolocation.

# Initialize a GeoIP object with the GeoLiteCity database for geolocation services.
gi = pygeoip.GeoIP('GeoLiteCity.dat')

def retKML(dstip, srcip):
    # Function to return KML (Keyhole Markup Language) data for a given destination and source IP address.

    # Get geolocation information for the destination IP address.
    dst = gi.record_by_name(dstip)
    # Get geolocation information for a specific public IP address.
    # This is commented out and instead uses a specific IP.
    src = gi.record_by_name('Your Public Ip Address(visit: https://www.whatsmyip.org/)')
    
    
    try:
        # Extract longitude and latitude from the destination's geolocation data.
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        # Extract longitude and latitude from the source's geolocation data.
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        
        # Create a KML Placemark element to represent the connection from src to dst.
        kml = (
            '<Placemark>\n'  # Start of Placemark element.
            '<name>%s</name>\n'  # Name element with the destination IP.
            '<extrude>1</extrude>\n'  # Extrude element to give height to the line.
            '<tessellate>1</tessellate>\n'  # Tessellate element for continuous line drawing.
            '<styleUrl>#transBluePoly</styleUrl>\n'  # Reference to a predefined style for the line.
            '<LineString>\n'  # Start of LineString element, which defines the path.
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'  # Coordinates for the line (dst to src).
            '</LineString>\n'  # End of LineString element.
            '</Placemark>\n'  # End of Placemark element.
        ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml  # Return the generated KML string.
    except:
        return ''  # Return an empty string if an error occurs (e.g., geolocation not found).

def plotIPs(pcap):
    # Function to iterate through a pcap file and generate KML for each packet.

    kmlPts = ''  # Initialize an empty string to store KML points.

    # Iterate over each packet in the pcap file.
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)  # Parse the Ethernet frame.
            ip = eth.data  # Extract the IP packet from the Ethernet frame.
            src = socket.inet_ntoa(ip.src)  # Convert source IP address from binary to human-readable form.
            dst = socket.inet_ntoa(ip.dst)  # Convert destination IP address from binary to human-readable form.
            
            # Generate KML for the current packet and add it to kmlPts.
            KML = retKML(dst, src)
            kmlPts = kmlPts + KML  # Append the KML data for this packet to the overall KML points.
        except:
            pass  # Ignore any errors that occur during parsing and continue with the next packet.
    return kmlPts  # Return the complete KML string for all packets.

def main():
    # Main function to read a pcap file, process it, and save the resulting KML document.

    f = open('wire6.pcap', 'rb')  # Open the pcap file in binary read mode.
    pcap = dpkt.pcap.Reader(f)  # Create a dpkt pcap Reader object to parse the pcap file.

    # Define the KML header and footer to wrap the generated KML placemarks.
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n' \
                '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'

    # Generate the complete KML document by combining the header, placemarks, and footer.
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter

    # Save the KML document to a file.
    with open('output1.kml', 'w') as outfile:
        outfile.write(kmldoc)  # Write the complete KML document to the output file.
    
    print("KML document has been saved to output.kml")  # Print a confirmation message.

if __name__ == '__main__':
    main()  # Call the main function if the script is executed directly.
