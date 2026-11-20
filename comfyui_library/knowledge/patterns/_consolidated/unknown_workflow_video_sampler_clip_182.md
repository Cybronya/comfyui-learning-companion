---
name: unknown_workflow_video_sampler_clip_182
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.973333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageConcanate, ImageResizeKJ, KSampler, LoadImage, ModelSamplingSD3, Primitive integer [Crystools], UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/720P高清FLF2V首尾帧ComfyUI原生支持_1913957506459103234.json, 视频生成/图生视频/WAN2.1-Fun-InP首尾帧视频生成ComfyUI原生版_1914626855226306562.json, 视频生成/图生视频/满血版Fun-InP万相首尾帧-ComfyUI原生_1914208993831780354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/720P高清FLF2V首尾帧ComfyUI原生支持_1913957506459103234.json、视频生成/图生视频/WAN2.1-Fun-InP首尾帧视频生成ComfyUI原生版_1914626855226306562.json、视频生成/图生视频/满血版Fun-InP万相首尾帧-ComfyUI原生_1914208993831780354.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageConcanate`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `Primitive integer [Crystools]`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 2/3 个有
- `SkipLayerGuidanceDiT` —— 2/3 个有
- `UNetTemporalAttentionMultiply` —— 2/3 个有
- `WanFunInpaintToVideo` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 3 - 6 | 3 | 72% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 3 - 6，3 个样本
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
