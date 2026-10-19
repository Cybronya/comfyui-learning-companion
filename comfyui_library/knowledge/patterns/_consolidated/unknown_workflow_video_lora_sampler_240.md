---
name: unknown_workflow_video_lora_sampler_240
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.460222
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/2064247414655115266.json, 视频生成/图生视频/2064232122084319234.json, 视频生成/图生视频/2013644132241121282.json, 视频生成/图生视频/2068809925526118401.json, 视频生成/文生视频/video_wan2_2_bernini_i2i_2064270918700060673.json, 视频生成/文生视频/video_wan2_2_bernini_multi_r2v_2064268091416207362.json, 视频生成/文生视频/video_wan2_2_bernini_r2v_2064265816681570306.json, 视频生成/文生视频/video_wan2_2_bernini_rv2v_change_style_2064258770699636737.json, 视频生成/文生视频/video_wan2_2_bernini_rv2v_changebg_2064251615900688385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_240

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2064247414655115266.json、视频生成/图生视频/2064232122084319234.json、视频生成/图生视频/2013644132241121282.json、视频生成/图生视频/2068809925526118401.json、视频生成/文生视频/video_wan2_2_bernini_i2i_2064270918700060673.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 8/9 个有
- `BatchImagesNode` —— 7/9 个有
- `BerniniConditioning` —— 7/9 个有
- `VHS_LoadVideo` —— 7/9 个有
- `CLIPVisionEncode` —— 2/9 个有
- `CM_IntToFloat` —— 1/9 个有
- `CR Seed` —— 1/9 个有
- `ComfyMathExpression` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/9 个有
- `WanImageToVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 78% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 9 | 90% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | lcm | - | 9 | 89% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，9 个样本，取值集中（一致性 90%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，9 个样本，一致性 89%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
