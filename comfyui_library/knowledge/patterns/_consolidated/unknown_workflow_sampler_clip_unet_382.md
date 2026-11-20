---
name: unknown_workflow_sampler_clip_unet_382
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.80775
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateVideo, DualCLIPLoader, HunyuanVideo15ImageToVideo, KSamplerSelect, ModelSamplingSD3, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/video_capybara_v0_1_video_edit_2027025679124013057.json, 平台全量/video_capybara_v0_1_video_edit_fast_2027033973167235074.json, 视频生成/图生视频/video_capybara_v0_1_image_to_video_2026952696527327234.json, 视频生成/图生视频/video_capybara_v0_1_image_to_video_fast_2027031167693754370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_382

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/video_capybara_v0_1_video_edit_2027025679124013057.json、平台全量/video_capybara_v0_1_video_edit_fast_2027033973167235074.json、视频生成/图生视频/video_capybara_v0_1_image_to_video_2026952696527327234.json、视频生成/图生视频/video_capybara_v0_1_image_to_video_fast_2027031167693754370.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `DualCLIPLoader`
- `HunyuanVideo15ImageToVideo`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ResizeAndPadImage` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
