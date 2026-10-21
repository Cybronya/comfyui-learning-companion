---
name: unknown_workflow_video_lora_sampler_32
type: Unknown Workflow
frequency: 26
level: strong
coverage: 0.944654
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2077642993561071617.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083124131020759041.json, 视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083420511694053378.json, 视频生成/图生视频/2053500201926705153.json, 视频生成/图生视频/2054607136101027841.json, 视频生成/图生视频/2063711056727461890.json, 视频生成/图生视频/2063712287315292162.json, 视频生成/图生视频/2063714093613281281.json, 视频生成/图生视频/2063914082952114178.json, 视频生成/图生视频/2070580986932449281.json, 视频生成/图生视频/2072973666828251138.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017.json, 视频生成/图生视频/2047152839029428226.json, 视频生成/图生视频/2047174431381921794.json, 视频生成/图生视频/2047224792201302017.json, 视频生成/图生视频/2048315037026099202.json, 视频生成/图生视频/2074392701696565250.json, 视频生成/图生视频/2075378321805897730.json, 视频生成/图生视频/2077654737146695682.json, 视频生成/图生视频/2077306195379056642.json, 视频生成/图生视频/1977014698942046209.json, 视频生成/图生视频/2020439963401195521.json, 视频生成/图生视频/2079086796184571905.json, 视频生成/图生视频/2078764896707244034.json, 视频生成/图生视频/首尾帧整理版  wan2.2 wan22  图生视频   视频生成_2087965953232556033.json, 视频生成/图生视频/2078441258510536706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/2077642993561071617.json、视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083124131020759041.json、视频生成/图生视频/首尾帧  图生视频   视频生成 wan2.2 wan22_2083420511694053378.json、视频生成/图生视频/2053500201926705153.json、视频生成/图生视频/2054607136101027841.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/26 个有
- `SetNode` —— 11/26 个有
- `PreviewAny` —— 2/26 个有
- `ImageConcatMulti` —— 1/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/26 个有
- `PreviewImage` —— 1/26 个有
- `VHS_SelectFilename` —— 1/26 个有
- `easy float` —— 1/26 个有
- `easy showAnything` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 26 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 26 | 100% |
| 采样算法 | 1 | 1 - 1 | 26 | 100% |
| 调度器 | euler | - | 26 | 100% |
| 重绘幅度 | beta | - | 26 | 69% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，26 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，26 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，26 个样本，一致性 100%
- 重绘幅度 最常用 beta，26 个样本，一致性 69%
