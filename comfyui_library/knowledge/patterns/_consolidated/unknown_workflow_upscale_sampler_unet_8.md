---
name: unknown_workflow_upscale_sampler_unet_8
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.815143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ColorTransfer, ComfyMathExpression, ImageConcatMulti, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MiniMax H3图生图2K加速+seedVR2超分细节翻倍_2116446087585288194.json, 图片生成/图生图/MiniMax H3图生图2K加速，再SeedVR2超分细节翻倍_2116396834464821250.json, 平台全量/H3一键转吉卜力动画电影风，SeedVR2超分2K细节直出_2117979820951953410.json, 平台全量/H3一键转手绘动画风，SeedVR2超分2K细节直出_2117494281727471618.json, 平台全量/H3一键转治愈手绘动画风，SeedVR2超分2K细节直出_2117970881522782209.json, 视频生成/图生视频/MiniMax_H3图生图2K加速+seedVR2超分细节翻倍_2116701727683604481.json, 视频生成/图生视频/MiniMax_H3图生图2K加速+seedVR2超分细节翻倍_2116715950119673857.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/MiniMax H3图生图2K加速+seedVR2超分细节翻倍_2116446087585288194.json、图片生成/图生图/MiniMax H3图生图2K加速，再SeedVR2超分细节翻倍_2116396834464821250.json、平台全量/H3一键转吉卜力动画电影风，SeedVR2超分2K细节直出_2117979820951953410.json、平台全量/H3一键转手绘动画风，SeedVR2超分2K细节直出_2117494281727471618.json、平台全量/H3一键转治愈手绘动画风，SeedVR2超分2K细节直出_2117970881522782209.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ColorTransfer`
- `ComfyMathExpression`
- `ImageConcatMulti`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 4/7 个有
- `PrimitiveFloat` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `Anything Everywhere3` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `ImageFromBatch+` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `MiniMaxChunkFeedForward` —— 3/7 个有
- `MiniMaxLowVRAMAttention` —— 3/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `SetNode` —— 3/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
