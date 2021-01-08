import cPickle, base64
try:
	from SimpleSession.versions.v62 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 10, 2, 40686])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v62 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDGFyb21hdGljTW9kZXEISwFLAX2HVQp2ZHdEZW5zaXR5cQlLAUdAFAAAAAAAAH2HVQZoaWRkZW5xCksBiX2HVQ1hcm9tYXRpY0NvbG9ycQtLAU59h1UPcmliYm9uU21vb3RoaW5ncQxLAUsAfYdVCWF1dG9jaGFpbnENSwGIfYdVCG9wdGlvbmFscQ59cQ9VCG9wZW5lZEFzcRCIiUsBKFUbZ3Vhbm9zaW5lX21vbm9waG9zcGhhdGUuc2RmcRFOTksBdHESfYeHc1UPbG93ZXJDYXNlQ2hhaW5zcRNLAYl9h1UJbGluZVdpZHRocRRLAUc/8AAAAAAAAH2HVQ9yZXNpZHVlTGFiZWxQb3NxFUsBSwB9h1UEbmFtZXEWSwFYBAAAADY4MDR9h1UPYXJvbWF0aWNEaXNwbGF5cRdLAYl9h1UPcmliYm9uU3RpZmZuZXNzcRhLAUc/6ZmZmZmZmn2HVQpwZGJIZWFkZXJzcRldcRp9cRthVQNpZHNxHEsBSwBLAIZ9h1UOc3VyZmFjZU9wYWNpdHlxHUsBR7/wAAAAAAAAfYdVEGFyb21hdGljTGluZVR5cGVxHksBSwJ9h1UUcmliYm9uSGlkZXNNYWluY2hhaW5xH0sBiH2HVQdkaXNwbGF5cSBLAYh9h3Uu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksBVQEgfYdVC2ZpbGxEaXNwbGF5cQNLAYl9h1UEbmFtZXEESwFYAwAAAFVOS32HVQVjaGFpbnEFSwFYAQAAACB9h1UOcmliYm9uRHJhd01vZGVxBksBSwJ9h1UCc3NxB0sBiYmGfYdVCG1vbGVjdWxlcQhLAUsAfYdVC3JpYmJvbkNvbG9ycQlLAU59h1UFbGFiZWxxCksBWAAAAAB9h1UKbGFiZWxDb2xvcnELSwFOfYdVCGZpbGxNb2RlcQxLAUsBfYdVBWlzSGV0cQ1LAYl9h1ULbGFiZWxPZmZzZXRxDksBTn2HVQhwb3NpdGlvbnEPXXEQSwFLAYZxEWFVDXJpYmJvbkRpc3BsYXlxEksBiX2HVQhvcHRpb25hbHETfVUEc3NJZHEUSwFK/////32HdS4='))
	atomInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQdyZXNpZHVlcQJLJksBfYdVCHZkd0NvbG9ycQNLJk59h1UEbmFtZXEESyZYAgAAAE84fXEFKFgCAAAATzddcQZLB2FYAgAAAE82XXEHSwZhWAIAAABPNV1xCEsFYVgCAAAATzRdcQlLBGFYAgAAAE8zXXEKSwNhWAIAAABPMl1xC0sCYVgCAAAATzFdcQxLAWFYAwAAAEMxMF1xDUsXYVgCAAAAQzldcQ5LFmFYAgAAAEM4XXEPSxVhWAIAAABDM11xEEsQYVgCAAAAQzJdcRFLD2FYAgAAAEMxXXESSw5hWAIAAABDN11xE0sUYVgCAAAAQzZdcRRLE2FYAgAAAEM1XXEVSxJhWAIAAABDNF1xFksRYVgCAAAAUDFdcRdLAGFYAwAAAEgxMF1xGEshYVgDAAAASDExXXEZSyJhWAMAAABIMTJdcRpLI2FYAwAAAEgxM11xG0skYVgDAAAASDE0XXEcSyVhWAIAAABOMV1xHUsJYVgCAAAATjJdcR5LCmFYAgAAAE4zXXEfSwthWAIAAABONF1xIEsMYVgCAAAATjVdcSFLDWFYAgAAAEg4XXEiSx9hWAIAAABIOV1xI0sgYVgCAAAASDJdcSRLGWFYAgAAAEgzXXElSxphWAIAAABIMV1xJksYYVgCAAAASDZdcSdLHWFYAgAAAEg3XXEoSx5hWAIAAABINF1xKUsbYVgCAAAASDVdcSpLHGF1h1UDdmR3cStLJol9h1UOc3VyZmFjZURpc3BsYXlxLEsmiX2HVQVjb2xvcnEtSyZLBH1xLihLAV1xL0sAYUsCXXEwKEsBSwJLA0sESwVLBksHSwhlSwNdcTEoSwlLCksLSwxLDWVOXXEyKEsOSw9LEEsRSxJLE0sUSxVLFksXZXWHVQlpZGF0bVR5cGVxM0smiX2HVQZhbHRMb2NxNEsmVQB9h1UFbGFiZWxxNUsmWAAAAAB9h1UOc3VyZmFjZU9wYWNpdHlxNksmR7/wAAAAAAAAfYdVB2VsZW1lbnRxN0smSwF9cTgoSwhdcTkoSwFLAksDSwRLBUsGSwdLCGVLB11xOihLCUsKSwtLDEsNZUsGXXE7KEsOSw9LEEsRSxJLE0sUSxVLFksXZUsPXXE8SwBhdYdVCmxhYmVsQ29sb3JxPUsmTn2HVQxzdXJmYWNlQ29sb3JxPksmTn2HVQ9zdXJmYWNlQ2F0ZWdvcnlxP0smWAQAAABtYWlufYdVBnJhZGl1c3FASyZHP/AAAAAAAAB9cUEoRz/9753AAAAAXXFCSwBhRz/4AAAAAAAAXXFDKEsBSwJLA0sESwVLBksIZUc/+gAAAAAAAF1xRChLCUsKSwtLDEsNZUc/+zMzQAAAAF1xRShLDksPSxBLEUsSSxNLFEsVSxZLF2VHP/euFIAAAABdcUZLB2F1h1UKY29vcmRJbmRleHFHXXFISwBLJoZxSWFVC2xhYmVsT2Zmc2V0cUpLJk59h1USbWluaW11bUxhYmVsUmFkaXVzcUtLJkcAAAAAAAAAAH2HVQhkcmF3TW9kZXFMSyZLAn2HVQhvcHRpb25hbHFNfXFOKFUGY2hhcmdlcU+IiUsmRwAAAAAAAAAAfXFQKEc/4AAAAAAAAF1xUShLJEslZUe/4euFHrhR7F1xUksBYUc/+Cj1wo9cKV1xU0sAYUe/5cKPXCj1w11xVChLAksDZUe/4ZmZmZmZml1xVUsEYUc/pHrhR64Ue11xVksUYUe/seuFHrhR7F1xV0sTYUe/6zMzMzMzM11xWEsNYUe/5R64UeuFH11xWUsMYUe/4PXCj1wo9l1xWksKYUc/wzMzMzMzM11xW0sgYUc/4ZmZmZmZml1xXEsXYUc/4UeuFHrhSF1xXUsPYUe/6KPXCj1wpF1xXihLBUsGZUc/0euFHrhR7F1xXyhLDksQSxFLEmVHP9mZmZmZmZpdcWAoSx5LH0shSyJLI2VHP6mZmZmZmZpdcWFLCWFHv+ZmZmZmZmZdcWJLCGFHv+I9cKPXCj1dcWMoSwdLC2VHP+vXCj1wo9ddcWRLFmFHP8HrhR64UexdcWVLFWF1h4dVDHNlcmlhbE51bWJlcnFmiIhdcWdLAUsmhnFoYYdVB2JmYWN0b3JxaYiJSyZHAAAAAAAAAAB9h4dVCW9jY3VwYW5jeXFqiIlLJkc/8AAAAAAAAH2Hh3VVB2Rpc3BsYXlxa0smiH2HdS4='))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECSyhOfYdVBWF0b21zcQNdcQQoXXEFKEsCSwZlXXEGKEsCSwdlXXEHKEsCSwhlXXEIKEsCSwplXXEJKEsDSxFlXXEKKEsDSxNlXXELKEsESxBlXXEMKEsESyBlXXENKEsFSxJlXXEOKEsFSyFlXXEPKEsGSxRlXXEQKEsHSyZlXXERKEsISydlXXESKEsJSxhlXXETKEsLSxFlXXEUKEsLSxVlXXEVKEsLSxZlXXEWKEsMSxVlXXEXKEsMSxllXXEYKEsMSyNlXXEZKEsNSxZlXXEaKEsNSxdlXXEbKEsOSxhlXXEcKEsOSxllXXEdKEsPSxllXXEeKEsPSyRlXXEfKEsPSyVlXXEgKEsQSxFlXXEhKEsQSxJlXXEiKEsQSxplXXEjKEsRSxtlXXEkKEsSSxNlXXElKEsSSxxlXXEmKEsTSxRlXXEnKEsTSx1lXXEoKEsUSx5lXXEpKEsUSx9lXXEqKEsVSxdlXXErKEsWSyJlXXEsKEsXSxhlZVUFbGFiZWxxLUsoWAAAAAB9h1UIaGFsZmJvbmRxLksoiH2HVQZyYWRpdXNxL0soRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cTBLKE59h1UIZHJhd01vZGVxMUsoSwF9h1UIb3B0aW9uYWxxMn1VB2Rpc3BsYXlxM0soSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('gAJ9cQFLAH1xAihLAF1xAyhHQBMkWhysCDFHP/ehYeT3Zf5HP76XjU/fO2SHcQRHP/NML4N7SiNHv+gk3S8an75HP/CNuLrHEMuHcQVHv+OOIZZSvTxHwAZHrhR64UhHv/TztkWhysGHcQZHP/U2ETQE6ktHwA3JhfBvaURHP9ZhfBvaURqHcQdHQA4MFUyYXwdHP9Z7sv7FbV1HP+Uxj8UEgW+HcQhHQA/qfvnbItFHQAFRGc4HX3BHv/G+De0ojOeHcQlHQBeyR0U47zVHP+MpXp4bCJpHv+PZf2K2rn2HcQpHwBDh5Pdl/YtHQAfruYx+KCRHv9tdzGPxQSCHcQtHQBUu5jH4oJBHQANnoPkJa7pHP/KhysCDEm+HcQxHv+svGp++dslHP6C+De0ojOdHP8ML4N7SiM6HcQ1HwAjkwvg3tKJHv+qj1wo9cKRHP9figkC3gDSHcQ5Hv/ZJUYKpkwxHQAFRTjvNNahHv9MrAgxJul6HcQ9HwBNYKpkwvg5HP+nWOIZZSvVHP6oCdSVGCqaHcRBHwBVWhysCDEpHv/cYk3S8an9HP+FT987ZFoeHcRFHP9jWoWHk92ZHv/4gW8AaNuNHv+wpx3mmtQuHcRJHv5Pdl/YrauhHv/JVmz0HyEtHP9i+De0ojOeHcRNHP/qNT987ZFpHwASaa1Cw8nxHv9uKCQLeANKHcRRHQAJbVz6rNnpHv/h41P3ztkZHP97CJoCdSVKHcRVHQAnSvTw2ETRHv+Ks2eg+QltHv9DGPxQSBbyHcRZHwAGaa1Cw8nxHP75jH4oJAt5HP8OYx+KCQLiHcRdHv9m6XjU/fO5HP/TiGWUr08NHv8DOcDr7fpGHcRhHwAQtDlYEGJNHP/aowVTJhfBHv76rNnoPkJeHcRlHwA9GCqZML4NHP/1Jul41P31Hv8eqzZ6D5CaHcRpHwBHF1jiGWUtHv9tNahYeT3ZHP9PIS13MY/GHcRtHP+NK9PDYRNBHv/Luy/sVtXRHv/sjOcDr7fqHcRxHv+JML4N7SiNHv/yc4HX2/SJHP/FTjvNNahaHcR1HQAJT987ZFodHwAc/sVtXPqtHv/QojOcDr7iHcR5HQAaRaHKwIMVHv/+yLQ5WBBlHP/VEZzgdfb+HcR9HQAV9itq59VpHv6KIznA6+39Hv/CjBVMmF8KHcSBHQBAuscQyylhHv/JWBBiTdLxHv+ckdFOO802HcSFHv+hOpKjBVMpHwAtxqfvnbItHv+MgW8AaNuOHcSJHQAFHeaa1Cw9HwBB2K2rn1WdHP+UfigkC3gGHcSNHP+TLKV6eGwlHP/i9PDYRNAVHv8pHRTjvNNeHcSRHwAcD5CWu5jJHv/zJ7sv7FbVHP+JRGc4HX3CHcSVHwBQVMmF8G9pHwAMZZSvTw2FHP+elEZzgdfeHcSZHwBlXCj1wo9dHv/R1jiGWUr1HP+C7mMfigkGHcSdHQBGQfIS13MZHQAd9v0h/y5JHv/j9If8uSOmHcShHQBrl41P3ztlHP/DQfIS13MZHv+7MzMzMzM2HcSllVQZhY3RpdmVxKksAdXMu'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'), 'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'),
'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), 'Eu': ((0.380392, 1, 0.780392), 1, u'default'),
'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), 'Er': ((0, 0.901961, 0.458824), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), 'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'),
'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), 'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'),
'Te': ((0.831373, 0.478431, 0), 1, u'default'), 'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), 'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 5, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (8, (u'H', (1, 1, 1, 1)), {(u'green', (0, 1, 0, 1)): [7], (u'N', (0.188235, 0.313725, 0.972549, 1)): [3], (u'P', (1, 0.501961, 0, 1)): [1], (u'O', (1, 0.0509804, 0.0509804, 1)): [2], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'yellow', (1, 1, 0, 1)): [5], (u'white', (1, 1, 1, 1)): [6]})
	viewerInfo = {'cameraAttrs': {'center': (0.19475, -0.37664999046326, -0.0725), 'fieldOfView': 13.43030742423, 'nearFar': (7.7478989223783, -7.8928989223783), 'ortho': False, 'eyeSeparation': 50.8, 'focal': -0.0725}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 9.62975, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 7, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 6}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v62 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.35740674433659325, 0.6604015517481455, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481455, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310294), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restoreRemainder():
	from SimpleSession.versions.v62 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (736, 611)
	xformMap = {0: (((0.083522864950297, -0.6692261385963, 0.73834971825686), 25.250871087177), (-0.1224352853963, -0.086176910363947, -0.064259109170827), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 80: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v62 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v62 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

