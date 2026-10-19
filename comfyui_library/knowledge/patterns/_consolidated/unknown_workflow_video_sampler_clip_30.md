---
name: unknown_workflow_video_sampler_clip_30
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.995231
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1935624782786527233.json, 视频生成/图生视频/1895181615108849666.json, 视频生成/图生视频/1902195474282258433.json, 视频生成/图生视频/1938538805421105153.json, 视频生成/图生视频/1910876944500752386.json, 视频生成/图生视频/1910598046382784514.json, 视频生成/图生视频/1902233258837303298.json, 视频生成/图生视频/1942457845642366977.json, 视频生成/图生视频/1902895670603460609.json, 视频生成/图生视频/1911283580138418178.json, 视频生成/图生视频/1911587726854975489.json, 视频生成/图生视频/1908814270581059585.json, 视频生成/图生视频/1897558094359285761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1935624782786527233.json、视频生成/图生视频/1895181615108849666.json、视频生成/图生视频/1902195474282258433.json、视频生成/图生视频/1938538805421105153.json、视频生成/图生视频/1910876944500752386.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCacheKJ` —— 11/13 个有
- `ImageResizeKJ` —— 10/13 个有
- `UNETLoader` —— 8/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `UnetLoaderGGUF` —— 6/13 个有
- `WanVideoEnhanceAVideoKJ` —— 6/13 个有
- `ImageUpscaleWithModel` —— 3/13 个有
- `UpscaleModelLoader` —— 3/13 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/13 个有
- `GIMMVFI_interpolate` —— 2/13 个有
- `ImageScaleBy` —— 2/13 个有
- `Int` —— 2/13 个有
- `LayerUtility: PurgeVRAM` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `WanVideoModelLoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 13 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 13 | 91% |
| 采样算法 | uni_pc | - | 13 | 92% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，13 个样本，取值集中（一致性 91%）
- 采样算法 最常用 uni_pc，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
