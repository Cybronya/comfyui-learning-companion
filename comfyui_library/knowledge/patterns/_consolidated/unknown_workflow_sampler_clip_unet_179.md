---
name: unknown_workflow_sampler_clip_unet_179
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.81875
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PreviewAny, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/文生图 布局可控 Ideogram4！_2063268058420039682.json, 图片生成/文生图/文生图_ideogram4_t2i_2062724777403572226.json, 图片生成/文生图/文生图_ideogram4_t2i_2062789809533448193.json, 图片生成/文生图/文生图_ideogram4_t2i_2070037043585044481.json, 图片生成/文生图/自动版ideogram4生图_2064619048377344001.json, 图片生成/文生图/自动版ideogram4生图_2069077763297996801.json, 图片生成/文生图/设计师福音 文生图精准编辑  ideogram4_2063246111061663745.json, 数字人/数字人/ideogram4-prompt-builder指定区域图片编辑_2064548694007042049.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_179

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/文生图 布局可控 Ideogram4！_2063268058420039682.json、图片生成/文生图/文生图_ideogram4_t2i_2062724777403572226.json、图片生成/文生图/文生图_ideogram4_t2i_2062789809533448193.json、图片生成/文生图/文生图_ideogram4_t2i_2070037043585044481.json、图片生成/文生图/自动版ideogram4生图_2064619048377344001.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `JsonExtractString`
- `KSamplerSelect`
- `PreviewAny`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `StringConcatenate` —— 5/8 个有
- `TextGenerate` —— 5/8 个有
- `CustomCombo` —— 4/8 个有
- `Ideogram4OptimizationsKJ` —— 3/8 个有
- `LoadImage` —— 3/8 个有
- `RH_LLMAPI_NODE` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `Ideogram4PromptBuilderKJ` —— 2/8 个有
- `ImpactSwitch` —— 2/8 个有
- `KSampler` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `Ideogram4DirectJSONBuilderModified` —— 1/8 个有
- `Int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
