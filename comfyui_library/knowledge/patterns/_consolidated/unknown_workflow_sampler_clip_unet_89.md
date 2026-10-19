---
name: unknown_workflow_sampler_clip_unet_89
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.807667
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateVideo, DualCLIPLoader, HunyuanVideo15ImageToVideo, KSamplerSelect, LoadImage, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2026952696527327234.json, 视频生成/图生视频/2027031167693754370.json, 视频生成/图生视频/1994018725741477890.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_89

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2026952696527327234.json、视频生成/图生视频/2027031167693754370.json、视频生成/图生视频/1994018725741477890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `DualCLIPLoader`
- `HunyuanVideo15ImageToVideo`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `ResizeAndPadImage` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `EasyCache` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
