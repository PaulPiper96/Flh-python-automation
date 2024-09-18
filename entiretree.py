from pdfquery import PDFQuery

def traverse_tree(element, level=0):
    """Recursively traverses the tree, printing the class name of each element."""
    # Print the class name of the current element
    print(f"{'  ' * level}Element Type: {type(element).__name__}")

    # If the element has children, recurse over them
    if hasattr(element, 'getchildren'):
        for child in element.getchildren():
            traverse_tree(child, level + 1)

# Load the PDF and parse it
pdf = PDFQuery('/Users/pc/Desktop/FLHMEDIA/CV.pdf')
pdf.load()

# Start the traversal from the root element
root = pdf.tree
traverse_tree(root)
