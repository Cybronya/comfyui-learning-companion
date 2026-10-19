---
name: text_to_image_lora_sampler_clip_8
type: Text To Image
frequency: 27
level: strong
coverage: 0.832815
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/FL2VA开源动作迁移｜MiniMax H3生成视频工作流_2094056951331254274.json, 视频生成/图生视频/FL2VA开源单图生视频｜MiniMax H3图生视频工作流_2093094312534962178.json, 视频生成/图生视频/H3图生视频 官方通用视频生成处理工具_2100635406244081666.json, 视频生成/图生视频/H3图生视频8步工作流 高效视频生成工具_2100275409492467713.json, 视频生成/图生视频/MiniMax H3 FL2VA开源人物模仿，动作迁移图生视频_2110821478810873857.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 用动作迁移直接生成视频_2095072427146571777.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 用动作迁移直接生成视频_2097466631751561218.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 用动作迁移直接生成视频_2106528532062101505.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版工作流 视频动作迁移人物图生视频方案_2094031469198008322.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版工作流 视频动作迁移人物图生视频方案_2097111204803203073.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版工作流 视频动作迁移人物图生视频方案_2098922083215564801.json, 视频生成/图生视频/MiniMax H3全能参考三图版｜三图输入视频生成_2094516324448948226.json, 视频生成/图生视频/MiniMax H3全能参考双图版｜双图输入视频生成_2094519227574218754.json, 视频生成/图生视频/MiniMax H3全能参考四图版｜多图输入视频生成_2094508021375397889.json, 视频生成/图生视频/MiniMax H3参考生视频 官方全能多模态创作工具_2098824046145269762.json, 视频生成/图生视频/MiniMax H3参考生视频加速版图生视频处理工具_2101358023905206274.json, 视频生成/图生视频/MiniMax H3参考生视频图生视频多模态处理工具_2101356055950356482.json, 视频生成/图生视频/MiniMax H3参考生视频｜多图参考保持主角一致性稳定输出_2099169349520150529.json, 视频生成/图生视频/MiniMax H3图生视频 官方全模态立体声视频生成_2098814736157728769.json, 视频生成/图生视频/MiniMax H3图生视频官方版｜高质量视频生成_2095962744792113153.json, 视频生成/图生视频/MiniMax H3图生视频工作流，图生视频高质量视频生成方案_2107902631598444546.json, 视频生成/图生视频/MiniMax H3多图参考｜图生视频多图生成_2090449654759645186.json, 视频生成/图生视频/MiniMax H3武打导演9组预设，视频生视频战斗特效_2111214317717770241.json, 视频生成/图生视频/Minimax H3 Veda稀疏注意力8步极速版参考生视频 快速出片_2108988281630314498.json, 视频生成/图生视频/Minimax H3 Veda稀疏注意力8步极速版首尾帧 视频生成控制_2108993138235895809.json, 视频生成/图生视频/Minimax H3参考图和参考视音频生成视频满血版 多模态输入_2105039400945147906.json, 视频生成/图生视频/MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/FL2VA开源动作迁移｜MiniMax H3生成视频工作流_2094056951331254274.json、视频生成/图生视频/FL2VA开源单图生视频｜MiniMax H3图生视频工作流_2093094312534962178.json、视频生成/图生视频/H3图生视频 官方通用视频生成处理工具_2100635406244081666.json、视频生成/图生视频/H3图生视频8步工作流 高效视频生成工具_2100275409492467713.json、视频生成/图生视频/MiniMax H3 FL2VA开源人物模仿，动作迁移图生视频_2110821478810873857.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 26/27 个有
- `PrimitiveBoolean` —— 26/27 个有
- `PrimitiveInt` —— 26/27 个有
- `MiniMaxH3ReferenceToVideo` —— 20/27 个有
- `VAEDecodeAudio` —— 19/27 个有
- `ResolutionSelector` —— 18/27 个有
- `GetImageSize` —— 13/27 个有
- `PrimitiveStringMultiline` —— 13/27 个有
- `SaveImage` —— 13/27 个有
- `GetVideoComponents` —— 11/27 个有
- `LoadVideo` —— 11/27 个有
- `ImageScale` —— 9/27 个有
- `LoadAudio` —— 8/27 个有
- `MiniMaxH3ImageToVideo` —— 8/27 个有
- `Video Slice` —— 8/27 个有
- `VideoFrameSample` —— 8/27 个有
- `ImageScaleToTotalPixels` —— 4/27 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/27 个有
- `Fast Bypasser (rgthree)` —— 2/27 个有
- `VedaSparseAttention` —— 2/27 个有
- `AnySwitch` —— 1/27 个有
- `BlockSparseAttention` —— 1/27 个有
- `CR Text` —— 1/27 个有
- `MiniMaxH3SigmaShift` —— 1/27 个有
- `MinimaxH3LatentUpscaler3DRefineHandoff` —— 1/27 个有
- `ModelAttentionBackend` —— 1/27 个有
- `PreviewAny` —— 1/27 个有
- `PreviewImage` —— 1/27 个有
- `QwenH3PromptLocal` —— 1/27 个有
- `SolAttnPatch` —— 1/27 个有
- `easy showAnything` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 高发问题（28/27 个样本）：Steps较低可能导致细节不足
