---
name: unknown_workflow_upscale_clip_checkpoint
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.681933
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, Image Comparer (rgthree), LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/8K图片高清放大_2083449760907878402.json, 图片生成/图生图/supir放大，适用于面部占比大的_1954064245321453570.json, 图片生成/图生图/【实用流】SUPIR  8K 效率放大_1819075068759814146.json, 图片生成/图生图/万物8k高清_2018494322525605889.json, 图片生成/图生图/图片SUP-模糊变高清_2046220648355205122.json, 图片生成/图生图/无损图片 一键高清放大_1908444757444730882.json, 图片生成/图生图/高清8K放大_1994687453787267073.json, 平台全量/1minute 8K Upscale_1862428643191402497.json, 平台全量/8k高清放大_1928028959160844289.json, 平台全量/Anime Upscaler Pro (Up to 16k)_1871085011209449473.json, 平台全量/SUPIR图片变清晰 工作流_1942499852515225601.json, 平台全量/supir高清放大_1839661197934153729.json, 平台全量/图片变清晰 supir 小白友好_1913823720211972098.json, 平台全量/图片高清放大_1940707386313306114.json, 平台全量/图生图sd3.5模型 +SUPIR高清放大修复_1848917154883158018.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/8K图片高清放大_2083449760907878402.json、图片生成/图生图/supir放大，适用于面部占比大的_1954064245321453570.json、图片生成/图生图/【实用流】SUPIR  8K 效率放大_1819075068759814146.json、图片生成/图生图/万物8k高清_2018494322525605889.json、图片生成/图生图/图片SUP-模糊变高清_2046220648355205122.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 13/15 个有
- `SetNode` —— 13/15 个有
- `ImpactInt` —— 11/15 个有
- `Seed (rgthree)` —— 11/15 个有
- `ImageResize+` —— 10/15 个有
- `Display Int (rgthree)` —— 9/15 个有
- `UltimateSDUpscale` —— 8/15 个有
- `HD UltimateSDUpscale` —— 7/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/15 个有
- `PreviewImage` —— 5/15 个有
- `CLIPLoader` —— 1/15 个有
- `DualCLIPLoader` —— 1/15 个有
- `EmptySD3LatentImage` —— 1/15 个有
- `KSampler` —— 1/15 个有
- `Note _O` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有
- `RH_Captioner` —— 1/15 个有
- `SeargePromptText` —— 1/15 个有
- `TripleCLIPLoader` —— 1/15 个有
- `VAEDecode` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 5.45 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | sgm_uniform | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
