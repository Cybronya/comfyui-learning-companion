---
name: image_to_image_sampler_clip_checkpoint_7
type: Image To Image
frequency: 5
level: strong
coverage: 0.84
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ICLightConditioning, KSampler, LoadAndApplyICLightUnet, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/一句话打光调色工作流 一键生图系列_1907267831539621890.json, 图片生成/图生图/打光-调画面色调【可在线运行】iclight_1917394858733146113.json, 平台全量/ICLight人像光影融合_1930083906245050369.json, 平台全量/一键更换人物背景，完美光照_1934218260592160769.json, 平台全量/一键更换人物背景，完美光照_1934224128037580801.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一句话打光调色工作流 一键生图系列_1907267831539621890.json、图片生成/图生图/打光-调画面色调【可在线运行】iclight_1917394858733146113.json、平台全量/ICLight人像光影融合_1930083906245050369.json、平台全量/一键更换人物背景，完美光照_1934218260592160769.json、平台全量/一键更换人物背景，完美光照_1934224128037580801.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ICLightConditioning`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 4/5 个有
- `InspyrenetRembg` —— 2/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `JjkText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 30 | 5 | 97% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 80% |
| 调度器 | karras | - | 5 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 5 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 30，5 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 80%
- 调度器 最常用 karras，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，5 个样本
