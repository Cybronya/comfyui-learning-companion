---
name: unknown_workflow_video_sampler_clip_53
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7379
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImageScaleBy, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, Pick From Batch (mtb), SaveImage, TT_img_enc, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/无审核Wan2.2超强图像编辑模型工作流加速版V1（时间戳强一致性）_1987188866065043458.json, 视频生成/图生视频/Comfy挑战赛8（诡影映画）-主题+扩写恐怖图生视频V1_1983771744160915457.json, 视频生成/图生视频/Gemini 3.1 Pro自导图生视频工作流-超高一致性WAN2.2模型_2044131826918236162.json, 视频生成/图生视频/Smooth 首尾＋图生 Qwen3 VL优化版_1983048736781795330.json, 视频生成/图生视频/Wan2.2 REMIX 图生视频-AIGC大赏_2033462929286242305.json, 视频生成/图生视频/Wan2.2 Smooth + Qwen3 VL无提示词自动扩写图生视频V2_1982721428191625217.json, 视频生成/图生视频/超高一致性WAN2.2多模态视频编辑_1987211259793838082.json, 视频生成/图生视频/（KJ版-（自用））Wan2.2 Remix V2 + Qwen VL3图生视频V2_1986359267705946114.json, 视频生成/图生视频/（KJ版）Wan2.2 Remix V2 + Qwen3 VL反推扩写图生视频V2_1986359186177093633.json, 视频生成/文生视频/Wan2.2 Smooth + Qwen3 VL反推扩写图生视频V2_1982707054148231169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/无审核Wan2.2超强图像编辑模型工作流加速版V1（时间戳强一致性）_1987188866065043458.json、视频生成/图生视频/Comfy挑战赛8（诡影映画）-主题+扩写恐怖图生视频V1_1983771744160915457.json、视频生成/图生视频/Gemini 3.1 Pro自导图生视频工作流-超高一致性WAN2.2模型_2044131826918236162.json、视频生成/图生视频/Smooth 首尾＋图生 Qwen3 VL优化版_1983048736781795330.json、视频生成/图生视频/Wan2.2 REMIX 图生视频-AIGC大赏_2033462929286242305.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `SaveImage`
- `TT_img_enc`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 9/10 个有
- `Seed (rgthree)` —— 9/10 个有
- `TT_img_enc_v2` —— 9/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `UnetLoaderGGUF` —— 8/10 个有
- `Qwen3_VQA` —— 7/10 个有
- `Text Concatenate` —— 7/10 个有
- `Any To Any` —— 6/10 个有
- `VHS_SelectFilename` —— 6/10 个有
- `GetImageRangeFromBatch` —— 3/10 个有
- `GetImageSize+` —— 3/10 个有
- `MathExpression_UTK` —— 3/10 个有
- `GetNode` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `RH_LLMAPI_NODE` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `easy imageListToImageBatch` —— 2/10 个有
- `ImageListToImageBatch` —— 1/10 个有
- `ImageLoader` —— 1/10 个有
- `MultiplePathsInput` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `Text` —— 1/10 个有
- `WanFirstLastFrameToVideo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 90% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler_ancestral | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 90%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
