---
key: 图片生成/图生图/Wan2.2局部洗图_1977364859492933633.json
name: Wan2.2局部洗图_1977364859492933633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2局部洗图_1977364859492933633.json
hash: 57ce6cf74035d52f
coverage: 0.8
learned_at: 2026-10-23 11:28:22
nodes: [UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, VAELoader, RandomNoise, SplitSigmas, SamplerCustomAdvanced, DisableNoise, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, CLIPTextEncode, WanVideoNAG, CFGGuider, CLIPLoader, RH_Captioner, VAEEncode, PreviewImage, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), ImageConcatMulti, PreviewImage, PreviewImage, InpaintStitch, Fast Groups Muter (rgthree), VAEDecode, LoadImage, InpaintCrop, BasicScheduler]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2局部洗图_1977364859492933633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2局部洗图_1977364859492933633.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `RandomNoise`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `CFGGuider`
- `CLIPLoader`
- `RH_Captioner`
- `VAEEncode` ★核心
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `PreviewImage`
- `PreviewImage`
- `InpaintStitch`
- `Fast Groups Muter (rgthree)`
- `VAEDecode` ★核心
- `LoadImage`
- `InpaintCrop`
- `BasicScheduler`

## 知识

覆盖率 **80%**（24/30）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAELoader`、`RandomNoise`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`ModelSamplingSD3`、`KSamplerSelect`、`WanVideoNAG`、`CFGGuider`、`CLIPLoader`、`RH_Captioner`、`VAEEncode`、`SaveImage`、`ImageConcatMulti`、`InpaintStitch`、`VAEDecode`、`LoadImage`、`InpaintCrop`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider
