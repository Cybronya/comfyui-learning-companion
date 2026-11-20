---
name: unknown_workflow_lora_sampler_clip_310
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.834
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Florence2ModelLoader, FluxGuidance, ImageScale, KSamplerSelect, LayerMask: MaskInvert, LayerUtility: ExtendCanvas, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, RandomNoise, RepeatLatentBatch, Replace Text _O, SaveImage, ShowText|pysssss, Text _O, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【华为PURAX】一键生成 模特手持产品模特图｜电商_1912032335100084226.json, "平台全量/ai自动生成模特手持产品图,电商神器_1897319904163352577.json"]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_310

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【华为PURAX】一键生成 模特手持产品模特图｜电商_1912032335100084226.json、平台全量/ai自动生成模特手持产品图,电商神器_1897319904163352577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `FluxGuidance`
- `ImageScale`
- `KSamplerSelect`
- `LayerMask: MaskInvert`
- `LayerUtility: ExtendCanvas`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `RandomNoise`
- `RepeatLatentBatch`
- `Replace Text _O`
- `SaveImage`
- `ShowText|pysssss`
- `Text _O`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
