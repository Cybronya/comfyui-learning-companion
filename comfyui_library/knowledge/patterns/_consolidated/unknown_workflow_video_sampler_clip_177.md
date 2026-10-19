---
name: unknown_workflow_video_sampler_clip_177
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.686
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageScale, KSampler, LoadImage, PreviewImage, ShowText|pysssss, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1900927379781337090.json, 视频生成/图生视频/1896189359580381186.json, 视频生成/图生视频/1900938287807086593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_177

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1900927379781337090.json、视频生成/图生视频/1896189359580381186.json、视频生成/图生视频/1900938287807086593.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LTXVPromptEnhancer` —— 2/3 个有
- `LTXVPromptEnhancerLoader` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `WanVideoTeaCacheKJ` —— 2/3 个有
- `DownloadAndLoadFlorence2Model` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `String Replace (mtb)` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
