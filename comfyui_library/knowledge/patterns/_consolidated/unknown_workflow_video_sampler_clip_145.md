---
name: unknown_workflow_video_sampler_clip_145
type: Unknown Workflow
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler]
problems: []
missing: []
members: [视频生成/图生视频/1997495774311288833.json, 视频生成/图生视频/2042064878357192705.json, 视频生成/图生视频/2044581787422171137.json, 视频生成/图生视频/1991489991482286081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_145

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1997495774311288833.json、视频生成/图生视频/2042064878357192705.json、视频生成/图生视频/2044581787422171137.json、视频生成/图生视频/1991489991482286081.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `WanFirstLastFrameToVideo` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `easy getNode` —— 1/4 个有
- `easy setNode` —— 1/4 个有
- `wanBlockSwap` —— 1/4 个有
- `wanBlock_Swap` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 4.5 | 3 - 8 | 4 | 58% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 1 | 1 - 1 | 4 | 100% |
| 重绘幅度 | euler_ancestral | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，4 个样本，一致性 100%
