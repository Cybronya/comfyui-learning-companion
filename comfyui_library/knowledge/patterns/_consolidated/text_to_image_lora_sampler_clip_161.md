---
name: text_to_image_lora_sampler_clip_161
type: Text To Image
frequency: 11
level: weak
coverage: 0.872455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Qwen2511-角色复刻极简工作流_2083813171214770177.json, 数字人/数字人/角色复刻极简工作流｜Qwen2511数字人快速生成_2088770876085985282.json, 视频生成/图生视频/H3 MAX旗舰模型图生视频 工作流让静态图片动起来_2098636207260524546.json, 视频生成/图生视频/H3 MAX旗舰模型图生视频｜让静态图片自然动起来_2098699818653802497.json, 视频生成/图生视频/H3 MAX首尾帧工作流｜旗舰模型双图过渡生成_2095597681195446273.json, 视频生成/图生视频/H3 Max Turbo图生视频 首尾帧视频生成工具_2099943877296877569.json, 视频生成/图生视频/H3 Max智能运镜工作流 AI看图自动运镜处理_2100658647239053314.json, 视频生成/图生视频/H3 Max智能运镜工作流 AI看图自动运镜处理_2100669399102476290.json, 视频生成/图生视频/H3极速版工作流 Turbo加速快速出片视频生成_2099936509838319618.json, 视频生成/图生视频/Kling 2.5首尾帧生视频｜两张图片变一段视频_2098769825513426945.json, 视频生成/文生视频/AI看图自动运镜｜H3 MAX智能运镜文生视频_2095836375957458946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/Qwen2511-角色复刻极简工作流_2083813171214770177.json、数字人/数字人/角色复刻极简工作流｜Qwen2511数字人快速生成_2088770876085985282.json、视频生成/图生视频/H3 MAX旗舰模型图生视频 工作流让静态图片动起来_2098636207260524546.json、视频生成/图生视频/H3 MAX旗舰模型图生视频｜让静态图片自然动起来_2098699818653802497.json、视频生成/图生视频/H3 MAX首尾帧工作流｜旗舰模型双图过渡生成_2095597681195446273.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `solarL_SaveImagesToZip` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `SaveVideo` —— 9/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `SaveImage` —— 7/11 个有
- `RH_MinimaxHailuoH3MaxImageToVideo` —— 6/11 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 3/11 个有
- `Image Comparer (rgthree)` —— 2/11 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 2/11 个有
- `ResizeImageMaskNode` —— 2/11 个有
- `TTResolutionSelector` —— 2/11 个有
- `TextEncodeQwenImageEditPlus` —— 2/11 个有
- `RH_Kling25_I2V_FirstLastFrame` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 76% |
| 采样算法 | er_sde | - | 11 | 91% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 512 | 11 | 0% |
| 高度 | 80 | 80 - 512 | 11 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 91%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 512，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 512，11 个样本，取值分散，一致性仅 0%
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
