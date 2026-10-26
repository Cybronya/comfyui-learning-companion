---
name: text_to_image_video_lora_sampler_24
type: Text To Image
frequency: 23
level: strong
coverage: 0.841174
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087143209582546946.json, 视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087154037660672001.json, 视频生成/图生视频/MiniMax-H3无限视频生成工作流｜分段接力长视频创作_2097784874290733057.json, 视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json, 视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2110652655700889602.json, 视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2107983189108154369.json, 视频生成/图生视频/Minimax H3双时钟采样参考图生视频｜4步turbo极速出片_2111270718934708225.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频 漫剧工作流，角色设计图生视频方案_2107927267103035393.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频短剧漫剧工作流，角色设计图生视频方案_2107965040040177666.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜SLA脸部动作稳定版_2097906883771330562.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意生成_2094540734518091777.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意视频制作_2107673663351910401.json, 视频生成/图生视频/minimax h3多参工作流｜多参考图生视频高质量生成_2097060954776367106.json, 视频生成/图生视频/全能参考二采高清放大｜H3 4步加速Lora图生视频_2096298417860468738.json, 视频生成/图生视频/双采加速图生视频｜MINIMAX-H3视频生成工作流_2088326770620715010.json, 视频生成/图生视频/双采加速工作流MINIMAX H3图生视频风扇变装模板_2088358447304761345.json, 视频生成/图生视频/反推提示词极速二次采样高质量图文生视频｜MiniMax_H3视频超分写实图生视频_2088172964058587138.json, 视频生成/图生视频/反推提示词极速二采高质量｜MiniMax H3文生视频写实_2097527914727305218.json, 视频生成/图生视频/反推提示词极速二采｜MiniMax_H3写实图文生视频超分_2091790249075761153.json, 视频生成/图生视频/四步加速出片｜H3全能参考二采高清放大带Lora_2096538998759059458.json, 视频生成/文生视频/4步加速二采放大｜MinimaxH3全能参考三模视频_2094739286921928705.json, 视频生成/文生视频/MinimaxH3全能参考二采高清放大｜4步加速生成_2094517725417787393.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087143209582546946.json、视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087154037660672001.json、视频生成/图生视频/MiniMax-H3无限视频生成工作流｜分段接力长视频创作_2097784874290733057.json、视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json、视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 22/23 个有
- `MiniMaxH3AVDecodeT8` —— 22/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 22/23 个有
- `RandomNoise` —— 22/23 个有
- `LoraLoaderBypassModelOnly` —— 20/23 个有
- `MiniMaxH3AudioConditioningT8` —— 18/23 个有
- `孤海注释` —— 18/23 个有
- `MiniMaxH3DualClockSamplerT8` —— 16/23 个有
- `CR Prompt Text` —— 13/23 个有
- `BasicScheduler` —— 10/23 个有
- `KSamplerSelect` —— 10/23 个有
- `PT_H3ConcatAVLatent` —— 10/23 个有
- `VAEEncode` —— 10/23 个有
- `Fast Groups Bypasser (rgthree)` —— 9/23 个有
- `LoadAudio` —— 9/23 个有
- `ModelAttentionBackend` —— 9/23 个有
- `ImageResizeKJv2` —— 8/23 个有
- `SolAttnMiniMax` —— 8/23 个有
- `SaveImage` —— 6/23 个有
- `VHS_LoadVideo` —— 6/23 个有
- `MiniMaxH3ReferenceToVideo` —— 5/23 个有
- `PrimitiveStringMultiline` —— 5/23 个有
- `CR Text` —— 4/23 个有
- `GetNode` —— 4/23 个有
- `SetNode` —— 4/23 个有
- `Dapao_LlamaCaption` —— 3/23 个有
- `Dapao_LlamaCaptionOptions` —— 3/23 个有
- `RegexReplace` —— 3/23 个有
- `easy promptConcat` —— 3/23 个有
- `easy showAnything` —— 3/23 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/23 个有
- `Label (rgthree)` —— 1/23 个有
- `PreviewImage` —— 1/23 个有
- `Text` —— 1/23 个有
- `workflow>运行采样` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高发问题（24/23 个样本）：Steps较低可能导致细节不足
