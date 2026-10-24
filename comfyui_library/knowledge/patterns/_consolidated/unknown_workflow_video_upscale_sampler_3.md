---
name: unknown_workflow_video_upscale_sampler_3
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.796
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageUpscaleWithModel, KSampler, LoadImage, RIFE VFI, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1图生视频（高清放大+补帧）_1921072224961495041.json, 视频生成/图生视频/吻屏电影运镜图生视频_1936559390805643265.json, 视频生成/图生视频/子弹时间电影运镜_1936425232217329665.json, 视频生成/图生视频/法相电影运镜图生视频_1937348192566452226.json, 视频生成/图生视频/法相电影运镜图生视频_1938115973906108418.json, 视频生成/图生视频/环绕移动电影运镜图生视频_1937707618603286529.json, 视频生成/图生视频/超英奔跑电影运镜图生视频_1934811898640539649.json, 视频生成/图生视频/车辆追逐电影运镜图生视频_1935544062428499969.json, 视频生成/图生视频/镜头推进电影运镜图生视频_1937714590371201026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/wan2.1图生视频（高清放大+补帧）_1921072224961495041.json、视频生成/图生视频/吻屏电影运镜图生视频_1936559390805643265.json、视频生成/图生视频/子弹时间电影运镜_1936425232217329665.json、视频生成/图生视频/法相电影运镜图生视频_1937348192566452226.json、视频生成/图生视频/法相电影运镜图生视频_1938115973906108418.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `RIFE VFI`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/9 个有
- `CR Text Concatenate` —— 8/9 个有
- `Florence2Run` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `Florence2ModelLoader` —— 7/9 个有
- `PathchSageAttentionKJ` —— 5/9 个有
- `TeaCache` —— 4/9 个有
- `WanVideoTeaCacheKJ` —— 2/9 个有
- `DownloadAndLoadFlorence2Model` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 9 | 100% |
| Prompt 约束强度(CFG) | 6 | 2 - 6 | 9 | 77% |
| 采样算法 | uni_pc | - | 9 | 89% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 2 - 6，9 个样本
- 采样算法 最常用 uni_pc，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
