---
name: unknown_workflow_video_lora_clip_5
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.976167
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/wan-SMOOTH V2.0_2010691930170068994.json, 视频生成/图生视频/wan2.2 图生视频 (加速版) 女孩拥抱_1950720072086147074.json, 视频生成/图生视频/wan2.2_fun_inpaint图生视频，首尾帧过渡工作流_1957002075188989954.json, 视频生成/图生视频/wan2.2首尾帧生视频_2042064878357192705.json, 视频生成/图生视频/wan2.2首尾帧生视频_2044581787422171137.json, 视频生成/图生视频/擦边流动感光波_1991489991482286081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/wan-SMOOTH V2.0_2010691930170068994.json、视频生成/图生视频/wan2.2 图生视频 (加速版) 女孩拥抱_1950720072086147074.json、视频生成/图生视频/wan2.2_fun_inpaint图生视频，首尾帧过渡工作流_1957002075188989954.json、视频生成/图生视频/wan2.2首尾帧生视频_2042064878357192705.json、视频生成/图生视频/wan2.2首尾帧生视频_2044581787422171137.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 5/6 个有
- `ModelSamplingSD3` —— 4/6 个有
- `WanMoeKSampler` —— 4/6 个有
- `Int` —— 3/6 个有
- `ModelPatchTorchSettings` —— 3/6 个有
- `WanFirstLastFrameToVideo` —— 3/6 个有
- `KSamplerAdvanced` —— 2/6 个有
- `WanImageToVideo` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `ImageListToBatch+` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/6 个有
- `WanFunInpaintToVideo` —— 1/6 个有
- `easy getNode` —— 1/6 个有
- `easy setNode` —— 1/6 个有
- `wanBlockSwap` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 50% |
| Prompt 约束强度(CFG) | 5 | 3 - 10 | 6 | 54% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 34% |
| 调度器 | 1 | 1 - 1 | 4 | 100% |
| 重绘幅度 | euler_ancestral | - | 6 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 5，观测区间 3 - 10，6 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 调度器 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，6 个样本，一致性 50%
