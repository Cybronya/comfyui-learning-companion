---
name: text_to_image_lora_sampler_clip_45
type: Text To Image
frequency: 19
level: strong
coverage: 0.910947
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/图像编辑文生图图生图｜MIniMax-H3图片编辑工作流_2088336424029474818.json, 视频生成/图生视频/8步极速图生视频t8版｜Minimax海螺h3 高质量出片就是这么快_2105519643300548609.json, 视频生成/图生视频/8步极速海螺h3图生视频｜Minimax高质量加速优化版 角色设计在线_2105518161696223233.json, 视频生成/图生视频/8步高质量极速MiniMax H3开源版工作流，文生视频视频生视频图生视频_2106140143164936194.json, 视频生成/图生视频/8步高质量极速Minimax H3开源版｜图生视频高效出片_2108379019711438850.json, 视频生成/图生视频/Dasiwa-MiniMax H3动态最强｜单采参考生视频_2095225077049683969.json, 视频生成/图生视频/Dasiwa参考图生视频｜MinimaxH3一键生成直出_2092358488738586626.json, 视频生成/图生视频/H3双时钟采样4步无损加速图生视频 极速高质量_2098839241043304449.json, 视频生成/图生视频/MiniMAX-H3-T8双时钟采样｜4步无损加速图生视频出片飞快_2099154403528896514.json, 视频生成/图生视频/MiniMax H3数字人加速版V1｜音频驱动打造音乐MV_2105223015419170818.json, 视频生成/图生视频/MiniMax H3音频驱动数字人 语音口型同步多人对话一键实现_2110352465429352449.json, 视频生成/图生视频/MiniMax H3音频驱动数字人加速版｜参考图生长视频直出_2103697575655333890.json, 视频生成/图生视频/MiniMax H3音频驱动数字人参考生视频长视频直出加速版，图生视频方案_2103992154782789634.json, 视频生成/图生视频/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具，数字人图生视频方案_2108327431890366466.json, 视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json, 视频生成/图生视频/加速版MiniMax H3图文一键生视频 快速出片方案_2109082909939429378.json, 视频生成/图生视频/参考图生视频｜Dasiwa MinimaxH3一键生成_2092617206365515777.json, 视频生成/图生视频/双时钟采样4步无损加速｜MiniMAX-H3-T8图生视频_2096272908212588545.json, 视频生成/图生视频/音频驱动数字人开口说话 MiniMax H3参考生视频长片直出_2104355836838637569.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/图像编辑文生图图生图｜MIniMax-H3图片编辑工作流_2088336424029474818.json、视频生成/图生视频/8步极速图生视频t8版｜Minimax海螺h3 高质量出片就是这么快_2105519643300548609.json、视频生成/图生视频/8步极速海螺h3图生视频｜Minimax高质量加速优化版 角色设计在线_2105518161696223233.json、视频生成/图生视频/8步高质量极速MiniMax H3开源版工作流，文生视频视频生视频图生视频_2106140143164936194.json、视频生成/图生视频/8步高质量极速Minimax H3开源版｜图生视频高效出片_2108379019711438850.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 18/19 个有
- `LoraLoaderBypassModelOnly` —— 18/19 个有
- `MiniMaxH3AVDecodeT8` —— 18/19 个有
- `MiniMaxH3AudioConditioningT8` —— 18/19 个有
- `PrimitiveFloat` —— 18/19 个有
- `VHS_VideoCombine` —— 18/19 个有
- `孤海注释` —— 18/19 个有
- `CR Prompt Text` —— 17/19 个有
- `ResolutionSelector` —— 17/19 个有
- `ModelAttentionBackend` —— 13/19 个有
- `SaveImage` —— 11/19 个有
- `LoadAudio` —— 9/19 个有
- `SolAttnMiniMax` —— 9/19 个有
- `easy int` —— 4/19 个有
- `GetImageSize` —— 3/19 个有
- `ImageScaleToTotalPixels` —— 3/19 个有
- `CM_IntToFloat` —— 2/19 个有
- `DuckHideNode` —— 2/19 个有
- `PrimitiveStringMultiline` —— 2/19 个有
- `ImageConcanate` —— 1/19 个有
- `MiniMaxH3StillConditioningT8` —— 1/19 个有
- `MiniMaxH3StillDecodeT8` —— 1/19 个有
- `MiniMaxH3StillPreflightT8` —— 1/19 个有
- `PreviewAny` —— 1/19 个有
- `PreviewImage` —— 1/19 个有
- `TimbreAudioLoader` —— 1/19 个有
- `WujiAudioLoader` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（22/19 个样本）：Steps较低可能导致细节不足
