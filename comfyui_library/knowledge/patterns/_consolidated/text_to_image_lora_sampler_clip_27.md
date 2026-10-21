---
name: text_to_image_lora_sampler_clip_27
type: Text To Image
frequency: 20
level: strong
coverage: 0.84155
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3无限视频生成工作流｜分段接力长视频创作_2097784874290733057.json, 视频生成/图生视频/MiniMaxH3双角色指定背景3图生视频加速版｜图生视频_2089717936046043138.json, 视频生成/图生视频/MiniMaxH3视频换背景编辑｜人物特效+运镜图生视频处理_2108372748677500929.json, 视频生成/图生视频/MiniMaxH3视频换背景，人物类特效视频生视频编辑器_2111274575668531202.json, 视频生成/图生视频/MiniMaxH3视频换背景｜视频编辑动作迁移生成_2095972447886598146.json, 视频生成/图生视频/MiniMaxH3视频背景替换编辑，其它视频处理全能手_2111278750330605570.json, 视频生成/图生视频/MiniMax_H3动作迁移图生视频_自定义背景人物全能参考_2101088561767473154.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理工具_2109456422231699458.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理方案_2109457359675412482.json, 视频生成/图生视频/Minimax H3参考生视频电商带货8步加速版工作流，服装展示图生视频方案_2108285549428699137.json, 视频生成/图生视频/Minimax H3电商带货参考生视频 8步加速版服装展示_2110352251444355074.json, 视频生成/图生视频/Minimax_H3单人极速人物替换，角色一致性动作迁移_2110892482811744258.json, 视频生成/图生视频/视频换背景提示词编辑｜MiniMaxH3视频生视频场景一键替换_2090468441949036546.json, 视频生成/图生视频/视频换背景支持参考图｜MiniMaxH3视频编辑实战_2101143111773802497.json, 视频生成/图生视频/视频换背景编辑｜MiniMaxH3人物特效动作迁移处理_2094593810511781890.json, 视频生成/图生视频/视频换背景随意换｜MiniMaxH3 视频编辑动作迁移_2096263348093542402.json, 视频生成/图生视频/视频编辑MiniMax H3视频换背景工作流，人物类特效视频运镜图生视频方案_2108448538760933377.json, 视频生成/文生视频/MiniMaxH3视频编辑｜文生视频换背景轻松搞定_2101170318881677313.json, 视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频音频参考_2085178835024306178.json, 视频生成/视频生视频/MiniMax H3视频换背景视频编辑工作流_人物特效视频生视频处理工具_2106155529885282305.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3无限视频生成工作流｜分段接力长视频创作_2097784874290733057.json、视频生成/图生视频/MiniMaxH3双角色指定背景3图生视频加速版｜图生视频_2089717936046043138.json、视频生成/图生视频/MiniMaxH3视频换背景编辑｜人物特效+运镜图生视频处理_2108372748677500929.json、视频生成/图生视频/MiniMaxH3视频换背景，人物类特效视频生视频编辑器_2111274575668531202.json、视频生成/图生视频/MiniMaxH3视频换背景｜视频编辑动作迁移生成_2095972447886598146.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 19/20 个有
- `BasicScheduler` —— 19/20 个有
- `KSamplerSelect` —— 19/20 个有
- `PrimitiveFloat` —— 19/20 个有
- `RandomNoise` —— 19/20 个有
- `VAEDecodeAudio` —— 19/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/20 个有
- `PathchSageAttentionKJ` —— 17/20 个有
- `PrimitiveStringMultiline` —— 17/20 个有
- `VHS_LoadVideo` —— 16/20 个有
- `VHS_VideoCombine` —— 16/20 个有
- `GetNode` —— 15/20 个有
- `SetNode` —— 15/20 个有
- `ImageConcanate` —— 14/20 个有
- `LayerUtility: PurgeVRAM V2` —— 13/20 个有
- `VRAM_Debug` —— 13/20 个有
- `孤海注释` —— 13/20 个有
- `SaveImage` —— 10/20 个有
- `LoadImage` —— 8/20 个有
- `EmptyImage` —— 7/20 个有
- `PreviewImage` —— 7/20 个有
- `CreateVideo` —— 5/20 个有
- `SaveVideo` —— 4/20 个有
- `LoadAudio` —— 2/20 个有
- `CR Prompt Text` —— 1/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `LoraLoaderBypassModelOnly` —— 1/20 个有
- `MuyeTextEditOutput` —— 1/20 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/20 个有
- `VHS_VideoInfoLoaded` —— 1/20 个有
- `workflow>运行采样` —— 1/20 个有

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
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
