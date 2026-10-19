---
name: text_to_image_lora_sampler_clip_33
type: Text To Image
frequency: 17
level: strong
coverage: 0.796941
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH38高动态加速流｜人物场景类特效图生视频_2092030919111692289.json, 视频生成/图生视频/MiniMaxH3视频换背景编辑｜人物特效+运镜图生视频处理_2108372748677500929.json, 视频生成/图生视频/MiniMaxH3视频换背景，人物类特效视频生视频编辑器_2111274575668531202.json, 视频生成/图生视频/MiniMaxH3视频换背景｜视频编辑动作迁移生成_2095972447886598146.json, 视频生成/图生视频/MiniMaxH3视频背景替换编辑，其它视频处理全能手_2111278750330605570.json, 视频生成/图生视频/MiniMax_H3动作迁移图生视频_自定义背景人物全能参考_2101088561767473154.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理工具_2109456422231699458.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理方案_2109457359675412482.json, 视频生成/图生视频/改版1｜数字人视频生成利器，老牌工作流焕新升级再战_2107327256866676738.json, 视频生成/图生视频/改版1｜数字人视频生成利器，老牌工作流焕新升级再战_2107440188136972289.json, 视频生成/图生视频/视频换背景提示词编辑｜MiniMaxH3视频生视频场景一键替换_2090468441949036546.json, 视频生成/图生视频/视频换背景支持参考图｜MiniMaxH3视频编辑实战_2101143111773802497.json, 视频生成/图生视频/视频换背景编辑｜MiniMaxH3人物特效动作迁移处理_2094593810511781890.json, 视频生成/图生视频/视频换背景随意换｜MiniMaxH3 视频编辑动作迁移_2096263348093542402.json, 视频生成/图生视频/视频编辑MiniMax H3视频换背景工作流，人物类特效视频运镜图生视频方案_2108448538760933377.json, 视频生成/文生视频/MiniMaxH3视频编辑｜文生视频换背景轻松搞定_2101170318881677313.json, 视频生成/视频生视频/MiniMax H3视频换背景视频编辑工作流_人物特效视频生视频处理工具_2106155529885282305.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH38高动态加速流｜人物场景类特效图生视频_2092030919111692289.json、视频生成/图生视频/MiniMaxH3视频换背景编辑｜人物特效+运镜图生视频处理_2108372748677500929.json、视频生成/图生视频/MiniMaxH3视频换背景，人物类特效视频生视频编辑器_2111274575668531202.json、视频生成/图生视频/MiniMaxH3视频换背景｜视频编辑动作迁移生成_2095972447886598146.json、视频生成/图生视频/MiniMaxH3视频背景替换编辑，其它视频处理全能手_2111278750330605570.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 17 个 workflow 都包含：
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
- `LoraLoaderModelOnly`
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

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 16/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/17 个有
- `PrimitiveStringMultiline` —— 15/17 个有
- `VHS_LoadVideo` —— 15/17 个有
- `VHS_VideoCombine` —— 14/17 个有
- `ImageConcanate` —— 13/17 个有
- `LayerUtility: PurgeVRAM V2` —— 13/17 个有
- `PathchSageAttentionKJ` —— 13/17 个有
- `VRAM_Debug` —— 13/17 个有
- `孤海注释` —— 11/17 个有
- `PreviewImage` —— 9/17 个有
- `EmptyImage` —— 7/17 个有
- `SaveImage` —— 6/17 个有
- `LoadImage` —— 5/17 个有
- `LoadAudio` —— 4/17 个有
- `CreateVideo` —— 3/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/17 个有
- `SaveVideo` —— 3/17 个有
- `Fast Groups Bypasser (rgthree)` —— 2/17 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 2/17 个有
- `MiniMaxH3SigmaShift` —— 2/17 个有
- `CR Prompt Text` —— 1/17 个有
- `FloatConstant` —— 1/17 个有
- `Text Multiline` —— 1/17 个有
- `easy clearCacheAll` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
