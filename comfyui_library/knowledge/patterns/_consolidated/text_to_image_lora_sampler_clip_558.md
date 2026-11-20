---
name: text_to_image_lora_sampler_clip_558
type: Text To Image
frequency: 3
level: strong
coverage: 0.916333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/收纳功能详解v2｜RunningHub实用技巧速览_2112456427628486658.json, 图片生成/文生图/Image-2.5图片编辑极速版 全能图片G2.5快速处理_2098306932686802946.json, 图片生成/文生图/独立站图片批量改尺寸｜反推提示词文生图工作流_2095950532711116801.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_558

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/收纳功能详解v2｜RunningHub实用技巧速览_2112456427628486658.json、图片生成/文生图/Image-2.5图片编辑极速版 全能图片G2.5快速处理_2098306932686802946.json、图片生成/文生图/独立站图片批量改尺寸｜反推提示词文生图工作流_2095950532711116801.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `ImageToMask` —— 1/3 个有
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 1/3 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/3 个有
- `TS_SVGStringToImage` —— 1/3 个有
- `VRGDG_PythonCodeRunner` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
