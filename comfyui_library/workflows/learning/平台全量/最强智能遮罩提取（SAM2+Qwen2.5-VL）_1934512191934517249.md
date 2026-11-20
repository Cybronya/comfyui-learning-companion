---
key: 平台全量/最强智能遮罩提取（SAM2+Qwen2.5-VL）_1934512191934517249.json
name: 最强智能遮罩提取（SAM2+Qwen2.5-VL）_1934512191934517249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强智能遮罩提取（SAM2+Qwen2.5-VL）_1934512191934517249.json
hash: 200ff7761601fd4a
coverage: 0.853659
learned_at: 2026-11-14 02:14:52
nodes: [InpaintModelConditioning, DifferentialDiffusion, ConditioningZeroOut, DualCLIPLoader, VAELoader, FluxGuidance, KSampler, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, easy showAnything, BBoxesToSAM2, LayerMask: LoadSAM2Model, LayerMask: LoadFlorence2Model, LayerUtility: LaMa, PreviewImage, VAEDecode, SaveImage, BlendInpaint, PreviewImage, Sam2Segmentation, MaskPreview+, DownloadAndLoadSAM2Model, LayerUtility: PurgeVRAM V2, LayerMask: LoadSAM2Model, LayerMask: ObjectDetectorFL2, PreviewImage, LayerMask: MaskPreview, LayerMask: MaskPreview, LayerMask: SAM2UltraV2, LayerMask: SegmentAnythingUltra, PreviewImage, Note, LayerMask: SAM2UltraV2, Miaoshouai_Tagger, GrowMaskWithBlur, LoadImage, DownloadAndLoadQwenModel, SaveImage, MaskPreview+, QwenVLDetection]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 997277281115137, "steps": 20}
---

# 平台全量/最强智能遮罩提取（SAM2+Qwen2.5-VL）_1934512191934517249.json

> 来源文件 `comfyui_library/workflows/平台全量/最强智能遮罩提取（SAM2+Qwen2.5-VL）_1934512191934517249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（41 个）：
- `InpaintModelConditioning`
- `DifferentialDiffusion`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `VAELoader`
- `FluxGuidance`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `BBoxesToSAM2`
- `LayerMask: LoadSAM2Model`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: LaMa`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `BlendInpaint`
- `PreviewImage`
- `Sam2Segmentation`
- `MaskPreview+`
- `DownloadAndLoadSAM2Model`
- `LayerUtility: PurgeVRAM V2`
- `LayerMask: LoadSAM2Model`
- `LayerMask: ObjectDetectorFL2`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `LayerMask: SAM2UltraV2`
- `LayerMask: SegmentAnythingUltra`
- `PreviewImage`
- `Note`
- `LayerMask: SAM2UltraV2`
- `Miaoshouai_Tagger`
- `GrowMaskWithBlur`
- `LoadImage`
- `DownloadAndLoadQwenModel`
- `SaveImage`
- `MaskPreview+`
- `QwenVLDetection`

## 关键参数

- `seed` = `997277281115137`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`InpaintModelConditioning`、`DifferentialDiffusion`、`ConditioningZeroOut`、`DualCLIPLoader`、`VAELoader`、`FluxGuidance`、`KSampler`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`BBoxesToSAM2`、`LayerMask: LoadSAM2Model`、`LayerMask: LoadFlorence2Model`、`LayerUtility: LaMa`、`VAEDecode`、`SaveImage`、`BlendInpaint`、`Sam2Segmentation`、`MaskPreview+`、`DownloadAndLoadSAM2Model`、`LayerUtility: PurgeVRAM V2`、`LayerMask: ObjectDetectorFL2`、`LayerMask: MaskPreview`、`LayerMask: SAM2UltraV2`、`LayerMask: SegmentAnythingUltra`、`Miaoshouai_Tagger`、`GrowMaskWithBlur`、`LoadImage`、`DownloadAndLoadQwenModel`、`QwenVLDetection`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
