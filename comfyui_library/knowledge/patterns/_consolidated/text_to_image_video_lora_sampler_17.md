---
name: text_to_image_video_lora_sampler_17
type: Text To Image
frequency: 20
level: strong
coverage: 0.6328
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/全行业广告制作加音频驱动加提示词生成器辅助扩写，数字人电商产品方案_2107226505611923457.json, 数字人/数字人/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2106927316462039041.json, 视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104675527998136322.json, 视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104762447012917250.json, 视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2105440243649441794.json, 视频生成/图生视频/H3最强二采吊打SelfLift虚空折叠流工作流，人物类特效图生视频方案_2107910096905920513.json, 视频生成/图生视频/H3最强二采唐僧彩蛋工作流，人物类特效场景类特效图生视频方案_2108293181078073346.json, 视频生成/图生视频/H3最强二采音画俱佳工作流，人物类特效战斗特效图生视频方案_2108346316232417282.json, 视频生成/图生视频/H3最强二采飓风京剧工作流，人物类特效场景类特效图生视频方案_2108289982774464514.json, 视频生成/图生视频/H3电影LORA巅峰双采去油PRO版视频生成处理工具_2101017420696739841.json, 视频生成/图生视频/H3电影感视频生成 每一帧电影级画面质感_2099578194558017538.json, 视频生成/图生视频/H3电影感视频生成 每帧电影级画面质感 高品质输出_2099579950520160258.json, 视频生成/图生视频/H3虚空折叠流最强二采 视频动态超越SelfLift_2110355960790343681.json, 视频生成/图生视频/H3超强工作流图生视频高质量视频生成方案 动态生成优化_2108717274050940929.json, 视频生成/图生视频/H3超强工作流，图生视频高质量视频生成方案_2107999971776749569.json, 视频生成/图生视频/MiniMax H3多参考生视频 快速高质量图生视频_2098830853072834562.json, 视频生成/图生视频/MiniMax H3多参考生视频快速高质量版｜图生视频速度画质兼得_2099143441149157378.json, 视频生成/图生视频/MiniMax H3多参考生视频｜字节DMAD加速双倍高清放大_2107644291471466498.json, 视频生成/图生视频/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2107981763464220673.json, 视频生成/图生视频/双倍高清放大MiniMax H3多参考生视频字节DMAD加速版工作流，图生视频_2107922679855669249.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（数字人/数字人/全行业广告制作加音频驱动加提示词生成器辅助扩写，数字人电商产品方案_2107226505611923457.json、数字人/数字人/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2106927316462039041.json、视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104675527998136322.json、视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104762447012917250.json、视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2105440243649441794.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 19/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/20 个有
- `MinimaxH3LatentUpscaler3D` —— 17/20 个有
- `VAEDecodeAudio` —— 17/20 个有
- `LoadAudio` —— 16/20 个有
- `PrimitiveFloat` —— 16/20 个有
- `SaveImage` —— 16/20 个有
- `SplitSigmas` —— 14/20 个有
- `Text` —— 14/20 个有
- `VHS_LoadVideo` —— 13/20 个有
- `easy float` —— 13/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/20 个有
- `easy showAnything` —— 5/20 个有
- `CR Text` —— 3/20 个有
- `INTConstant` —— 3/20 个有
- `LTXVAudioVAEEncode` —— 3/20 个有
- `ManualSigmas` —— 3/20 个有
- `MultiTextConcatenate` —— 3/20 个有
- `MuyeTextEditOutput` —— 3/20 个有
- `RHLLMChatNode` —— 3/20 个有
- `SetLatentNoiseMask` —— 3/20 个有
- `SolidMask` —— 3/20 个有
- `SoundFlow_GetLength` —— 3/20 个有
- `Astra` —— 2/20 个有
- `ImageFromBatch` —— 2/20 个有
- `Int` —— 2/20 个有
- `LoadVideo` —— 2/20 个有
- `MiniMaxH3AVDecodeT8` —— 2/20 个有
- `SaveVideo` —— 2/20 个有
- `获取视频信息` —— 2/20 个有
- `EmptyImage` —— 1/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `Float` —— 1/20 个有
- `MiniMaxH3VoiceLibraryLoadT8` —— 1/20 个有
- `PreviewImage` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（23/20 个样本）：Steps较低可能导致细节不足
