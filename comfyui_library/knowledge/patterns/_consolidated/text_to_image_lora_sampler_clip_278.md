---
name: text_to_image_lora_sampler_clip_278
type: Text To Image
frequency: 7
level: strong
coverage: 0.885
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/DLSS5超分放大视频生成_视频超分辨率增强处理_2100422243741425665.json, 视频生成/图生视频/H3_Max_Turbo图生视频_首尾帧视频生成工具_2100424763167563778.json, 视频生成/图生视频/H3极速版Turbo加速视频生成处理工作流_2101019073734864897.json, 视频生成/图生视频/H3极速版工作流 Turbo加速快速出片视频生成_2099936509838319618.json, 视频生成/图生视频/H3极速版工作流_Turbo加速快速出片视频生成_2100509732602728450.json, 视频生成/图生视频/Kling 2.5首尾帧生视频｜两张图片变一段视频_2098769825513426945.json, 视频生成/图生视频/全能视频图生视频低价版6-30秒处理生成工具_2102169806098231298.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_278

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/DLSS5超分放大视频生成_视频超分辨率增强处理_2100422243741425665.json、视频生成/图生视频/H3_Max_Turbo图生视频_首尾帧视频生成工具_2100424763167563778.json、视频生成/图生视频/H3极速版Turbo加速视频生成处理工作流_2101019073734864897.json、视频生成/图生视频/H3极速版工作流 Turbo加速快速出片视频生成_2099936509838319618.json、视频生成/图生视频/H3极速版工作流_Turbo加速快速出片视频生成_2100509732602728450.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `SaveImage` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `EmptyImage` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `RH_DLSS5Enhance` —— 1/7 个有
- `RH_Kling25_I2V_FirstLastFrame` —— 1/7 个有
- `RH_RhartVideoGImageToVideo` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
