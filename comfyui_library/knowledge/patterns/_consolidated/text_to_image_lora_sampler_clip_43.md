---
name: text_to_image_lora_sampler_clip_43
type: Text To Image
frequency: 16
level: strong
coverage: 0.896437
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3 Native vs DMAD文生视频工作流，文生视频图生视频方案_2106848580148482050.json, 视频生成/文生视频/MiniMax H3文生视频加速版 官方Turbo加速出片_2099198028581265410.json, 视频生成/文生视频/MiniMax H3文生视频基础版｜一句话生成高质量视频片段_2099177157141553154.json, 视频生成/文生视频/MiniMax H3文生视频官方版｜高质量视频生成_2095959827330723842.json, 视频生成/文生视频/MiniMax H3文生视频纯净版｜从零开始生成完整短片_2107694082242990081.json, 视频生成/文生视频/MiniMax H3文生视频｜官方加速版工作流生成_2096331392543191041.json, 视频生成/文生视频/MiniMax H3超级加速文生视频，角色一致性角色表演视频生成方案_2103903431479095298.json, 视频生成/文生视频/Minimax H3潜空间放大FL2VA版｜文生图生视频工作流_2097781976299294722.json, 视频生成/文生视频/REF2VA-Upscale双采样｜MiniMax_H3视频生成角色表演_2092872749298569217.json, 视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json, 视频生成/文生视频/一键直出1080P竖屏｜动漫短剧三模视频工作流_2094052576818978817.json, 视频生成/文生视频/一键直出1080P竖屏｜动漫短剧工作流文生视频_2093846854189539329.json, 视频生成/文生视频/两步生成768P视频｜Minimax H3 多参数加速LoRA_2096256232272257025.json, 视频生成/文生视频/多参数视频生成768p｜Minimax H3加速LoRA两步_2095964673219846146.json, 视频生成/文生视频/多参生视频潜空间放大二采｜Minimax H3高质量版_2095969486913495042.json, 视频生成/文生视频/多参生视频潜空间放大｜Minimax H3 二采画质更稳_2096260116558467073.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Native vs DMAD文生视频工作流，文生视频图生视频方案_2106848580148482050.json、视频生成/文生视频/MiniMax H3文生视频加速版 官方Turbo加速出片_2099198028581265410.json、视频生成/文生视频/MiniMax H3文生视频基础版｜一句话生成高质量视频片段_2099177157141553154.json、视频生成/文生视频/MiniMax H3文生视频官方版｜高质量视频生成_2095959827330723842.json、视频生成/文生视频/MiniMax H3文生视频纯净版｜从零开始生成完整短片_2107694082242990081.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 15/16 个有
- `PrimitiveFloat` —— 15/16 个有
- `ResolutionSelector` —— 15/16 个有
- `CreateVideo` —— 13/16 个有
- `SaveVideo` —— 13/16 个有
- `LTXVSeparateAVLatent` —— 10/16 个有
- `LTXVConcatAVLatent` —— 9/16 个有
- `MiniMaxH3ImageToVideo` —— 9/16 个有
- `MiniMaxH3SigmaShift` —— 9/16 个有
- `ModelAttentionBackend` —— 9/16 个有
- `LoadImage` —— 8/16 个有
- `MinimaxH3LatentUpscaler3D` —— 8/16 个有
- `VHS_VideoCombine` —— 8/16 个有
- `ManualSigmas` —— 7/16 个有
- `MiniMaxH3ReferenceToVideo` —— 7/16 个有
- `SplitSigmas` —— 7/16 个有
- `ModelPreviewOverrideKJ` —— 6/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/16 个有
- `PrimitiveStringMultiline` —— 5/16 个有
- `SaveImage` —— 4/16 个有
- `ComfySwitchNode` —— 3/16 个有
- `PrimitiveBoolean` —— 3/16 个有
- `PrimitiveInt` —— 3/16 个有
- `GetVideoComponents` —— 2/16 个有
- `LoadVideo` —— 2/16 个有
- `Seed (rgthree)` —— 2/16 个有
- `Text` —— 2/16 个有
- `AddLabel` —— 1/16 个有
- `CR Text` —— 1/16 个有
- `ImageConcanate` —— 1/16 个有
- `PainterVRAM` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
