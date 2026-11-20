---
name: text_to_image_video_lora_sampler_26
type: Text To Image
frequency: 21
level: strong
coverage: 0.90819
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458.json, 视频生成/图生视频/8步极速图生视频t8版｜Minimax海螺h3 高质量出片就是这么快_2105519643300548609.json, 视频生成/图生视频/8步极速海螺h3图生视频｜Minimax高质量加速优化版 角色设计在线_2105518161696223233.json, 视频生成/图生视频/8步高质量极速MiniMax H3开源版工作流，文生视频视频生视频图生视频_2106140143164936194.json, 视频生成/图生视频/8步高质量极速Minimax H3开源版｜图生视频高效出片_2108379019711438850.json, 视频生成/图生视频/Dasiwa-MiniMax H3动态最强｜单采参考生视频_2095225077049683969.json, 视频生成/图生视频/Dasiwa参考图生视频｜MinimaxH3一键生成直出_2092358488738586626.json, 视频生成/图生视频/H3双时钟采样4步无损加速图生视频 极速高质量_2098839241043304449.json, 视频生成/图生视频/Lightx2v正式版8步去油双时钟参考生视频V2｜Minimax图生视频工作流_2088144409752850433.json, 视频生成/图生视频/MiniMAX-H3-T8双时钟采样｜4步无损加速图生视频出片飞快_2099154403528896514.json, 视频生成/图生视频/MiniMax H3全能参考工作流｜文生视频单图生视频图生视频_2090446719375990786.json, 视频生成/图生视频/MiniMax H3数字人加速版V1｜音频驱动打造音乐MV_2105223015419170818.json, 视频生成/图生视频/MiniMax H3视频复刻加速版，数字人参考生视频与长视频直出工作流_2102827221554651137.json, 视频生成/图生视频/MiniMax H3视频复刻数字人加速版｜参考生视频长视频直出｜口播福音_2102608437405372417.json, 视频生成/图生视频/MiniMax H3视频复刻数字人换人换产品文案不换原声保留_2108718797380218882.json, 视频生成/图生视频/MiniMax H3视频复刻数字人视频换人换产品换文案语音替换_2108676232131997697.json, 视频生成/图生视频/MiniMax H3音频驱动数字人 语音口型同步多人对话一键实现_2110352465429352449.json, 视频生成/图生视频/MiniMax H3音频驱动数字人参考生视频长视频直出加速版，图生视频方案_2103992154782789634.json, 视频生成/图生视频/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具，数字人图生视频方案_2108327431890366466.json, 视频生成/图生视频/h3开源加速版MINIMAX-H3合集｜单图生多图参考4步lora加速_2097965293799825409.json, 视频生成/图生视频/参考图生视频｜Dasiwa MinimaxH3一键生成_2092617206365515777.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（数字人/数字人/AI短剧人物开口说话V1.1｜8秒有声测试版先睹为快_2112399633505939458.json、视频生成/图生视频/8步极速图生视频t8版｜Minimax海螺h3 高质量出片就是这么快_2105519643300548609.json、视频生成/图生视频/8步极速海螺h3图生视频｜Minimax高质量加速优化版 角色设计在线_2105518161696223233.json、视频生成/图生视频/8步高质量极速MiniMax H3开源版工作流，文生视频视频生视频图生视频_2106140143164936194.json、视频生成/图生视频/8步高质量极速Minimax H3开源版｜图生视频高效出片_2108379019711438850.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 20/21 个有
- `ResolutionSelector` —— 20/21 个有
- `MiniMaxH3DualClockSamplerT8` —— 18/21 个有
- `CR Prompt Text` —— 17/21 个有
- `ModelAttentionBackend` —— 14/21 个有
- `SaveImage` —— 10/21 个有
- `SolAttnMiniMax` —— 10/21 个有
- `LoadAudio` —— 8/21 个有
- `PrimitiveStringMultiline` —— 4/21 个有
- `VHS_LoadVideo` —— 4/21 个有
- `Fast Groups Bypasser (rgthree)` —— 3/21 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/21 个有
- `PreviewImage` —— 3/21 个有
- `easy int` —— 3/21 个有
- `CM_IntToFloat` —— 2/21 个有
- `DuckHideNode` —— 2/21 个有
- `EmptyImage` —— 2/21 个有
- `GetImageSize` —— 2/21 个有
- `ImageScaleToTotalPixels` —— 2/21 个有
- `UniBlockSwap` —— 2/21 个有
- `StringFormat` —— 1/21 个有
- `TimbreAudioLoader` —— 1/21 个有
- `WujiAudioLoader` —— 1/21 个有
- `YuanCustomCombo` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（25/21 个样本）：Steps较低可能导致细节不足
