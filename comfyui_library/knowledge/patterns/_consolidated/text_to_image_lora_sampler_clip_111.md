---
name: text_to_image_lora_sampler_clip_111
type: Text To Image
frequency: 10
level: strong
coverage: 0.8821
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3角色替换｜单人指定角色+视频编辑多合一_2110716972131512322.json, 视频生成/图生视频/MiniMax H3超燃角色PV制作｜人物特效美少女_2095264146601365505.json, 视频生成/图生视频/MiniMax参考生视频视频生视频图生视频_2086540228310945793.json, 视频生成/图生视频/Minimax H3 高动态打斗模型｜更稳更有冲击力_2096914596027260929.json, 视频生成/图生视频/Minimax H3三图参考无参考音｜图生视频多图参考_2089732304192237570.json, 视频生成/图生视频/Minimax H3单人极速人物替换，角色一致性动作迁移_2110538185297186818.json, 视频生成/图生视频/Minimax H3双图参考双参考音｜图生视频多模态参考_2089737749720031234.json, 视频生成/图生视频/Minimax H3双图参考无参考音｜图生视频多图参考_2089736461087232001.json, 视频生成/图生视频/Minimax H3完美人物替换 图生视频换人方案_2110363954835976194.json, 视频生成/图生视频/Minimax-H3多参长视频736p直出｜原版图生视频工作流_2097088563040051202.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3角色替换｜单人指定角色+视频编辑多合一_2110716972131512322.json、视频生成/图生视频/MiniMax H3超燃角色PV制作｜人物特效美少女_2095264146601365505.json、视频生成/图生视频/MiniMax参考生视频视频生视频图生视频_2086540228310945793.json、视频生成/图生视频/Minimax H3 高动态打斗模型｜更稳更有冲击力_2096914596027260929.json、视频生成/图生视频/Minimax H3三图参考无参考音｜图生视频多图参考_2089732304192237570.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `VHS_VideoCombine` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `MiniMaxH3SigmaShift` —— 7/10 个有
- `ModelAttentionBackend` —— 5/10 个有
- `ModelPreviewOverrideKJ` —— 4/10 个有
- `VHS_LoadVideo` —— 4/10 个有
- `INTConstant` —— 3/10 个有
- `LoadAudio` —— 3/10 个有
- `SaveImage` —— 3/10 个有
- `BlockSparseAttention` —— 2/10 个有
- `CreateVideo` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ManualSigmas` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LoadVideoUI` —— 1/10 个有
- `MiniMaxH3MotionContext` —— 1/10 个有
- `MiniMaxH3MotionContextTrim` —— 1/10 个有
- `MiniMaxH3Unified` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `SaveVideo` —— 1/10 个有
- `VHS_VideoInfoLoaded` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
