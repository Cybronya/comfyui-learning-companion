---
name: unknown_workflow_lora_sampler_clip_176
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.848333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Aspect Ratio, DepthAnythingV2Preprocessor, DualCLIPLoader, FluxGuidance, JanusImageUnderstanding, JanusModelLoader, KSamplerSelect, LayerColor: Brightness & Contrast, LayerFilter: FilmV2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringFunction|pysssss, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/维克多油画生成器_1943094958733606913.json, 图片生成/图生图/皮神deepseek超清网红生成器_1898372485853696001.json, 图片生成/文生图/【网红大片】小红书+抖音网红生成+高清放大修复_1908795586177282049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_176

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/维克多油画生成器_1943094958733606913.json、图片生成/图生图/皮神deepseek超清网红生成器_1898372485853696001.json、图片生成/文生图/【网红大片】小红书+抖音网红生成+高清放大修复_1908795586177282049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Aspect Ratio`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LayerFilter: FilmV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
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
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `SUPIR_Upscale` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
