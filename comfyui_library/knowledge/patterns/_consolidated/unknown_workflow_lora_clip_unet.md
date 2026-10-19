---
name: unknown_workflow_lora_clip_unet
type: Unknown Workflow
frequency: 62
level: moderate
coverage: 0.742823
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyHunyuanLatentVideo, ImpactInt, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR Text Concatenate, CR Simple Image Compare, Text Multiline, LayerUtility: GetImageSize]
members: [图片生成/文生图/1950107467746295810.json, 图片生成/文生图/1950564507682787330.json, 图片生成/文生图/1950782044102119425.json, 图片生成/文生图/1950856807457685505.json, 图片生成/文生图/1971551023703715842.json, 图片生成/文生图/1972896298716319746.json, 图片生成/文生图/1972939909457686529.json, 图片生成/文生图/1972947059097645057.json, 图片生成/文生图/1974015925068410881.json, 图片生成/文生图/1974019322081357825.json, 图片生成/文生图/1974021462468202497.json, 图片生成/文生图/1975025203577270274.json, 图片生成/文生图/1975817514456322050.json, 图片生成/文生图/1975852667996123138.json, 图片生成/文生图/1976909357554274305.json, 图片生成/文生图/1976940810480570369.json, 图片生成/文生图/1976941262408437762.json, 图片生成/文生图/1976941283002458114.json, 图片生成/文生图/1976943281324085250.json, 图片生成/文生图/1976943296230629378.json, 图片生成/文生图/1976943344981024770.json, 图片生成/文生图/1976945241829842945.json, 图片生成/文生图/1976945289019969538.json, 图片生成/文生图/1976945342690271233.json, 图片生成/文生图/1976949154444386305.json, 图片生成/文生图/1976949173209702401.json, 图片生成/文生图/1976949219397390338.json, 图片生成/文生图/1976951052618604546.json, 图片生成/文生图/1976951076974940161.json, 图片生成/文生图/1976951105995329538.json, 图片生成/文生图/1976996175272386562.json, 图片生成/文生图/1977261443643002881.json, 图片生成/文生图/1977267467867312129.json, 图片生成/文生图/1977267506425536513.json, 图片生成/文生图/1977267518844882945.json, 图片生成/文生图/1978046581360447490.json, 图片生成/文生图/1978057115090694146.json, 图片生成/文生图/1978059541503946754.json, 图片生成/文生图/1978060652960960513.json, 图片生成/文生图/1978067565324947458.json, 图片生成/文生图/1978748046857097218.json, 图片生成/文生图/1978755480703094785.json, 图片生成/文生图/1978982498640236545.json, 图片生成/文生图/1979580429642665985.json, 图片生成/文生图/1980445101136764930.json, 图片生成/文生图/1980465314754420737.json, 图片生成/文生图/1980467585336717314.json, 图片生成/文生图/1980601353535930369.json, 图片生成/文生图/1981018910998806529.json, 图片生成/文生图/1981643153134501889.json, 图片生成/文生图/1981653086898929665.json, 图片生成/文生图/1981885057533132801.json, 图片生成/文生图/1982066220537135106.json, 图片生成/文生图/1985616134449901570.json, 图片生成/文生图/1985619406799745025.json, 图片生成/文生图/1985947534256418818.json, 图片生成/文生图/1986027656405811201.json, 图片生成/文生图/1986413389037662210.json, 视频生成/图生视频/1979523155746263042.json, 视频生成/文生视频/1950782044102119425.json, 视频生成/文生视频/1979514191478427649.json, 视频生成/文生视频/枫叶妈妈（终极1）_1980804630861008898.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet

> 由 `engine/knowledge_consolidation` 从 62 个 workflow 归纳得出（图片生成/文生图/1950107467746295810.json、图片生成/文生图/1950564507682787330.json、图片生成/文生图/1950782044102119425.json、图片生成/文生图/1950856807457685505.json、图片生成/文生图/1971551023703715842.json…）

- **类型**：Unknown Workflow
- **样本数**：62
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 62 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 59/62 个有
- `KSampler` —— 58/62 个有
- `LoadImage` —— 58/62 个有
- `easy showAnything` —— 58/62 个有
- `UltimateSDUpscale` —— 57/62 个有
- `UpscaleModelLoader` —— 57/62 个有
- `PrimitiveFloat` —— 56/62 个有
- `LayerUtility: GetImageSize` —— 52/62 个有
- `PreviewImage` —— 48/62 个有
- `FL_SDUltimate_Slices` —— 5/62 个有
- `KSamplerAdvanced` —— 5/62 个有
- `PurgeVRAM_UTK` —— 5/62 个有
- `ImpactSwitch` —— 3/62 个有
- `CR Simple Image Compare` —— 2/62 个有
- `Text Multiline` —— 2/62 个有
- `Wan_video_prompt_generator` —— 2/62 个有
- `Image Comparer (rgthree)` —— 1/62 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 12 | 58 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 62 | 0% |
| 采样算法 | res_2s | - | 62 | 92% |
| 调度器 | bong_tangent | - | 62 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 58 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/62 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 12，58 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，62 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 res_2s，62 个样本，一致性 92%
- 调度器 最常用 bong_tangent，62 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，58 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、CR Simple Image Compare、Text Multiline、LayerUtility: GetImageSize
