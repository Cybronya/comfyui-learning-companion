---
name: unknown_workflow_upscale_lora_sampler_99
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.844
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Aspect Ratio, DepthAnythingV2Preprocessor, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), JanusImageUnderstanding, JanusModelLoader, KSamplerSelect, LayerColor: Brightness & Contrast, LayerFilter: FilmV2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SUPIR_Upscale, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/皮神deepseek超清网红生成器_1898372485853696001.json, 图片生成/文生图/【网红大片】小红书+抖音网红生成+高清放大修复_1908795586177282049.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_99

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/皮神deepseek超清网红生成器_1898372485853696001.json、图片生成/文生图/【网红大片】小红书+抖音网红生成+高清放大修复_1908795586177282049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Aspect Ratio`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LayerFilter: FilmV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SUPIR_Upscale`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
