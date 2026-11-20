---
name: text_to_image_lora_sampler_clip_300
type: Text To Image
frequency: 7
level: strong
coverage: 0.921
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片去水印免蒙版｜YOLO自动检测标记，一键擦除更省心_2100192477151055873.json, 图片生成/图生图/图片去水印｜LaMa修复引擎补图，擦除痕迹几乎看不见_2099935925890543617.json, 图片生成/图生图/图片去水印｜LaMa修复引擎补图，擦除痕迹几乎看不见_2100193279357837314.json, 图片生成/图生图/多参考图生成图片三参考版｜1张底图配3张参考图自由组合_2113496822227496961.json, 图片生成/图生图/多参考图生成图片单参考版｜1张底图配1张参考图图生图实操_2113447812187901953.json, 图片生成/图生图/多参考图生成图片双参考版｜1张底图配2张参考图组合出图_2113570269372706818.json, 图片生成/图生图/多参考图生成图片四参考版｜1张底图配4张参考图灵活拼图_2113498813825642497.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_300

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图片去水印免蒙版｜YOLO自动检测标记，一键擦除更省心_2100192477151055873.json、图片生成/图生图/图片去水印｜LaMa修复引擎补图，擦除痕迹几乎看不见_2099935925890543617.json、图片生成/图生图/图片去水印｜LaMa修复引擎补图，擦除痕迹几乎看不见_2100193279357837314.json、图片生成/图生图/多参考图生成图片三参考版｜1张底图配3张参考图自由组合_2113496822227496961.json、图片生成/图生图/多参考图生成图片单参考版｜1张底图配1张参考图图生图实操_2113447812187901953.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `孤海注释` —— 5/7 个有
- `TextEncodeQwenImage21` —— 4/7 个有
- `ImageScale` —— 3/7 个有
- `LayerUtility: LaMa` —— 3/7 个有
- `EmptyImage` —— 2/7 个有
- `ImageToMask` —— 2/7 个有
- `WatermarkDetector` —— 1/7 个有
- `WatermarkDetectorLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
