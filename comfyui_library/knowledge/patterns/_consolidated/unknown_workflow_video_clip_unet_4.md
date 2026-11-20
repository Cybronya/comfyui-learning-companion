---
name: unknown_workflow_video_clip_unet_4
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.9045
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 SmoothMix图生视频高动态（官方版）_1980507194548469761.json, 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_1980673656160436226.json, 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_2049663225859457025.json, 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_2050777904669306881.json, 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）（双图）_1983902184238710786.json, 视频生成/图生视频/Wan2.2-SmoothMix高动态图生视频，动态加强_1979742422047559681.json, 视频生成/图生视频/Wan2.2RemixV2.0图生视频_1989285733921902593.json, 视频生成/图生视频/Wan2.2SmoothMix首尾帧高动态视频生成_1979871682087260162.json, 视频生成/图生视频/Wan2.2_14B_首尾帧工作流【ComfyUI版】_1955942871625027585.json, 视频生成/图生视频/video_wan2_2_14B_首尾帧工作流_1952189425302360065.json, 视频生成/图生视频/wan2.2 首尾帧 极速版_1952583825614409730.json, 视频生成/图生视频/wan2.2 首尾帧视频 lightx2v 加速_1995400759510544385.json, 视频生成/图生视频/万相首尾帧_1953403463789150209.json, 视频生成/图生视频/首尾帧生视频_自动提示词_1955867522656555010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 SmoothMix图生视频高动态（官方版）_1980507194548469761.json、视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_1980673656160436226.json、视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_2049663225859457025.json、视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）_2050777904669306881.json、视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）（双图）_1983902184238710786.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 13/14 个有
- `CLIPVisionEncode` —— 12/14 个有
- `CLIPVisionLoader` —— 12/14 个有
- `CR Text` —— 12/14 个有
- `WanFirstLastFrameToVideo` —— 11/14 个有
- `SimpleMath+` —— 10/14 个有
- `PrimitiveInt` —— 8/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `WanVideoNAG` —— 6/14 个有
- `PathchSageAttentionKJ` —— 5/14 个有
- `ImageResizeKJ` —— 4/14 个有
- `ImageResizeKJv2` —— 4/14 个有
- `ImpactInt` —— 4/14 个有
- `WanImageToVideo` —— 2/14 个有
- `ApplySageAttention` —— 1/14 个有
- `DeepTranslatorTextNode` —— 1/14 个有
- `Joy_caption_two` —— 1/14 个有
- `Joy_caption_two_load` —— 1/14 个有
- `LayerUtility: TextJoin` —— 1/14 个有
- `PainterI2V` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `WanMoeKSampler` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 71% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 14 | 100% |
| 采样算法 | 1 | 1 - 1.5 | 14 | 84% |
| 调度器 | uni_pc | - | 14 | 43% |
| 重绘幅度 | simple | - | 14 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，14 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.5，14 个样本，取值集中（一致性 84%）
- 调度器 最常用 uni_pc，14 个样本，一致性 43%
- 重绘幅度 最常用 simple，14 个样本，一致性 93%
