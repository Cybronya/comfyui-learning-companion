---
name: text_to_image_video_lora_sampler_37
type: Text To Image
frequency: 18
level: strong
coverage: 0.919889
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax_H3视频复刻工作流，视频编辑翻拍二创角色替换长视频直出_2116813560327262210.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜换人换产品文案不换原声保留_2107986135334088706.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2107984724403777537.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2110652655700889602.json, 视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话加速版长视频处理工具，数字人生成方案_2109462993590382594.json, 视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2107983189108154369.json, 视频生成/图生视频/Minimax-H3lora)ENG8步多参生视频(双时钟图生极速2分钟出5秒ENG_2087129153064751106.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜SLA脸部动作稳定版_2097906883771330562.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意生成_2094540734518091777.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意视频制作_2107673663351910401.json, 视频生成/图生视频/Minimax海螺H3加速版｜图生视频8步高质量，极速出片_2099892617046740993.json, 视频生成/图生视频/Minimax海螺h3图生视频8步极速优化版t8｜高质量加速_2100809902179573761.json, 视频生成/图生视频/SLA脸部动作稳定版｜Minimax-H3开源参考生视频角色一致_2091613796845572097.json, 视频生成/图生视频/SLA脸部动作稳定｜Minimax-H3参考生视频角色一致性_2091785773665316865.json, 视频生成/图生视频/Seedance2.5文生视频工作流｜视频运镜高质量生成_2097809713382649858.json, 视频生成/图生视频/minimax h3多参工作流｜多参考图生视频高质量生成_2097060954776367106.json, 视频生成/图生视频/minmax生图工作流｜图生视频配套生图方案_2097990295555235841.json, 视频生成/图生视频/音频驱动数字人开口说话 MiniMax H3参考生视频长片直出_2104355836838637569.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3视频复刻工作流，视频编辑翻拍二创角色替换长视频直出_2116813560327262210.json、视频生成/图生视频/MiniMax_H3视频复刻数字人｜换人换产品文案不换原声保留_2107986135334088706.json、视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2107984724403777537.json、视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2110652655700889602.json、视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话加速版长视频处理工具，数字人生成方案_2109462993590382594.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 15/18 个有
- `ModelAttentionBackend` —— 12/18 个有
- `SolAttnMiniMax` —— 12/18 个有
- `孤海注释` —— 12/18 个有
- `SaveImage` —— 7/18 个有
- `PreviewImage` —— 6/18 个有
- `VHS_LoadVideo` —— 5/18 个有
- `LoadAudio` —— 4/18 个有
- `EmptyImage` —— 3/18 个有
- `Fast Groups Bypasser (rgthree)` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/18 个有
- `MiniMaxH3TurboLoRA` —— 2/18 个有
- `PrimitiveStringMultiline` —— 2/18 个有
- `AnyBooleanSwitch` —— 1/18 个有
- `CR Font File List` —— 1/18 个有
- `CR Text` —— 1/18 个有
- `CompressImages` —— 1/18 个有
- `ImpactConditionalBranch` —— 1/18 个有
- `LoadFolderFromDir` —— 1/18 个有
- `LoadVideo` —— 1/18 个有
- `VHS_SelectFilename` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（21/18 个样本）：Steps较低可能导致细节不足
