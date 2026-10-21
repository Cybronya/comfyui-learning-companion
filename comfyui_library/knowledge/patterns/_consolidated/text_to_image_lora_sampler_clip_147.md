---
name: text_to_image_lora_sampler_clip_147
type: Text To Image
frequency: 8
level: strong
coverage: 0.886875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/DLSS5超分放大视频生成_视频超分辨率增强处理_2100422243741425665.json, 视频生成/图生视频/H3_Max_Turbo图生视频_首尾帧视频生成工具_2100424763167563778.json, 视频生成/图生视频/H3极速版Turbo加速视频生成处理工作流_2101019073734864897.json, 视频生成/图生视频/H3极速版工作流 Turbo加速快速出片视频生成_2099936509838319618.json, 视频生成/图生视频/H3极速版工作流_Turbo加速快速出片视频生成_2100509732602728450.json, 视频生成/图生视频/MiniMax H3 Max Turbo极速版图生视频首尾帧处理工具_2102123247629332481.json, 视频生成/图生视频/MiniMax H3 Max Turbo极速版图生视频首尾帧，高速低成本流畅过渡方案_2103565859515101186.json, 视频生成/图生视频/MiniMax_H3上下文参考视频加图生视频｜融合运镜与角色一致性_2101908397733011457.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_147

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/DLSS5超分放大视频生成_视频超分辨率增强处理_2100422243741425665.json、视频生成/图生视频/H3_Max_Turbo图生视频_首尾帧视频生成工具_2100424763167563778.json、视频生成/图生视频/H3极速版Turbo加速视频生成处理工作流_2101019073734864897.json、视频生成/图生视频/H3极速版工作流 Turbo加速快速出片视频生成_2099936509838319618.json、视频生成/图生视频/H3极速版工作流_Turbo加速快速出片视频生成_2100509732602728450.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoadImage` —— 7/8 个有
- `SaveImage` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 6/8 个有
- `EmptyImage` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `孤海注释` —— 5/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `RH_DLSS5Enhance` —— 1/8 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/8 个有
- `RH_MinimaxHailuoH3MultimodalToVideo` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有
- `VHS_VideoInfoLoaded` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
