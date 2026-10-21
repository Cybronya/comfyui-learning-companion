---
name: unknown_workflow_clip_unet_vae_11
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9435
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1949897152581558273.json, 视频生成/图生视频/1950103025572601857.json, 视频生成/图生视频/2011418883764260865.json, 视频生成/图生视频/1955829466150965249.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1949897152581558273.json、视频生成/图生视频/1950103025572601857.json、视频生成/图生视频/2011418883764260865.json、视频生成/图生视频/1955829466150965249.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `Wan22ImageToVideoLatent` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `WanImageToVideo` —— 1/4 个有
- `WanMoeKSampler` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 3 | 59% |
| Prompt 约束强度(CFG) | 5 | 1 - 10 | 4 | 39% |
| 采样算法 | uni_pc | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 10，4 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 uni_pc，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
