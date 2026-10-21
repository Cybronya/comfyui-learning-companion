---
name: text_to_image_lora_sampler_clip_10
type: Text To Image
frequency: 31
level: strong
coverage: 0.553645
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/海螺480全能参考v2｜视频图生视频一键直出_2090200734355775489.json, 视频生成/图生视频/满血int8单采八步加速｜MinimaxH3 Sigma版V4生成_2093254483198439425.json, 视频生成/文生视频/MiniMax H3 全能视频生成｜文生图生视频多合一极速二采优化_2097497016648683521.json, 视频生成/文生视频/MiniMax H3多参考7P3A2V二采优化版｜多素材混合生视频，画面节奏更耐看_2100487458340294657.json, 视频生成/文生视频/MiniMax H3多参考7P3A2V生视频优化版｜文生视频视频生视频全都能接_2100485687203155970.json, 视频生成/文生视频/MiniMax H3多参考生视频9图片3视频3音频处理工具_2102119756018044929.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版，文生视频视频生视频图生视频方案_2107247870394064897.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜文生视频图生视频画质更稳_2104532274321645569.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜文生视频视频生视频_2106990754123051010.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜高质量生成_2095587743173799938.json, 视频生成/文生视频/MiniMax H3多参考生视频最新优化版 多模态输入方案_2105415601509462017.json, 视频生成/文生视频/MiniMax H3多参考生视频｜优化版高质量生成_2095226419768029186.json, 视频生成/文生视频/MiniMax H3多参考生视频｜最新优化版效果再升级_2105135308315648002.json, 视频生成/文生视频/MiniMax H3多合一极速生视频｜二采优化全能工作流_2097533751998898178.json, 视频生成/文生视频/MiniMax H3多图多音频视频参考｜无水印优化版_2095227965956247554.json, 视频生成/文生视频/MiniMax H3武戏全能视频V3｜打斗高质量生成_2095598787678007297.json, 视频生成/文生视频/lin多模态工作流｜文生视频视频生视频图生视频通吃_2101150805402406913.json, 视频生成/文生视频/万象动漫短剧文戏生成｜12秒横屏MiniMax H3制作_2096310040830496769.json, 视频生成/文生视频/万象动漫短剧文戏生成｜12秒竖屏多参视频制作_2096742818462134273.json, 视频生成/文生视频/十二秒横屏文戏专用｜万象动漫短剧文生视频三模输入_2096618054703730690.json, 视频生成/文生视频/多参考出片更稳｜MiniMax H3优化版人物角色视频_2096626000930103297.json, 视频生成/文生视频/多参考图输入视频生成 MiniMax H3优化版角色一致性更强_2104770269930934274.json, 视频生成/文生视频/多参考生视频优化升级｜文生视频视频生视频一键生成_2095569186260078594.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3人物角色一致性_2096301587214987265.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3数字人图生视频_2095829921988964354.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3文生视频升级_2095564235781795841.json, 视频生成/文生视频/多参考生视频优化版｜角色一致性高质量视频生成_2095231061662978049.json, 视频生成/文生视频/多参考生视频双采工作流｜MiniMax H3高清放大生成_2096723203140972545.json, 视频生成/文生视频/多参考生视频双采工作流｜MiniMax H3高清放大生成_2097087018537938945.json, 视频生成/文生视频/多图多音频参考生视频｜MiniMax H3无水印优化版_2095565882998222850.json, 视频生成/文生视频/混合模型sigma强化潜空间放大｜minimaxH3高清直出不油腻_2091282726027616257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（视频生成/图生视频/海螺480全能参考v2｜视频图生视频一键直出_2090200734355775489.json、视频生成/图生视频/满血int8单采八步加速｜MinimaxH3 Sigma版V4生成_2093254483198439425.json、视频生成/文生视频/MiniMax H3 全能视频生成｜文生图生视频多合一极速二采优化_2097497016648683521.json、视频生成/文生视频/MiniMax H3多参考7P3A2V二采优化版｜多素材混合生视频，画面节奏更耐看_2100487458340294657.json、视频生成/文生视频/MiniMax H3多参考7P3A2V生视频优化版｜文生视频视频生视频全都能接_2100485687203155970.json…）

- **类型**：Text To Image
- **样本数**：31
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 31 个 workflow 都包含：
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 30/31 个有
- `VHS_VideoCombine` —— 30/31 个有
- `LTXVConcatAVLatent` —— 29/31 个有
- `LTXVSeparateAVLatent` —— 29/31 个有
- `MinimaxH3LatentUpscaler3D` —— 29/31 个有
- `SplitSigmas` —— 28/31 个有
- `LoadAudio` —— 27/31 个有
- `VHS_LoadVideo` —— 27/31 个有
- `easy float` —— 27/31 个有
- `Text` —— 23/31 个有
- `忽略多组孤海` —— 8/31 个有
- `SaveImage` —— 6/31 个有
- `ModelAttentionBackend` —— 4/31 个有
- `Text Multiline` —— 4/31 个有
- `H3SigmaRefiner` —— 3/31 个有
- `INTConstant` —— 2/31 个有
- `MiniMaxH3SigmaShift` —— 2/31 个有
- `ModelPreviewOverrideKJ` —— 2/31 个有
- `ResizeShortestToNode` —— 2/31 个有
- `SolAttnMiniMax` —— 2/31 个有
- `图像缩放范围孤海` —— 2/31 个有
- `CM_IntToFloat` —— 1/31 个有
- `CR Prompt Text` —— 1/31 个有
- `CreateVideo` —— 1/31 个有
- `ExtendIntermediateSigmas` —— 1/31 个有
- `Fast Groups Bypasser (rgthree)` —— 1/31 个有
- `FloatConstant` —— 1/31 个有
- `PathchSageAttentionKJ` —— 1/31 个有
- `PrimitiveStringMultiline` —— 1/31 个有
- `SaveVideo` —— 1/31 个有
- `easy showAnything` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 31 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 31 | 100% |
| 采样算法 | er_sde | - | 31 | 100% |
| 调度器 | beta | - | 31 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 31 | 100% |
| 宽度 | 80 | 80 - 80 | 31 | 100% |
| 高度 | 80 | 80 - 80 | 31 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/31 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，31 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，31 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，31 个样本，一致性 100%
- 调度器 最常用 beta，31 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，31 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，31 个样本，取值集中（一致性 100%）
- 高发问题（31/31 个样本）：Steps较低可能导致细节不足
