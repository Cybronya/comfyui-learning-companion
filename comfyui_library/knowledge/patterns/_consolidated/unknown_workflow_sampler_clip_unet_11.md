---
name: unknown_workflow_sampler_clip_unet_11
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.81156
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PreviewAny, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/VividMuse Ideogram4 workflow_2064337095640047618.json, 图片生成/文生图/ideogram4-prompt-builder-fixed_2063828351755833345.json, 图片生成/文生图/ideogram4_2063180809263206402.json, 图片生成/文生图/ideogram4_t2i文生图+Ideogram 4 Prompt Builder KJ_2064175389697724418.json, 图片生成/文生图/ideogram4工作流_2062533863087362049.json, 图片生成/文生图/ideogram4工作流_2062836963702562817.json, 图片生成/文生图/ideogram4工作流带提示词_2063538368042070017.json, 图片生成/文生图/ideogram4工作流带提示词_2063769707022479362.json, 图片生成/文生图/ideogram4工作流带提示词_2063772030377480194.json, 图片生成/文生图/ideogram4工作流带提示词_2063804440662073345.json, 图片生成/文生图/ideogram4工作流带提示词_2063810498231095297.json, 图片生成/文生图/ideogram4工作流带提示词_2063812502248583169.json, 图片生成/文生图/ideogram4工作流带提示词_2063813597683343362.json, 图片生成/文生图/ideogram4工作流带提示词_2063815460910616578.json, 图片生成/文生图/ideogram4工作流带提示词_2063816739921686529.json, 图片生成/文生图/ideogram4工作流带提示词_2063817989841047554.json, 图片生成/文生图/ideogram4工作流带提示词_2064174515973869569.json, 图片生成/文生图/ideogram4工作流带提示词_2064177318440034306.json, 图片生成/文生图/ideogram4工作流文生图工作流_2062820277763010562.json, 图片生成/文生图/ideogram4工作流文生图工作流_2062872647050022914.json, 图片生成/文生图/文生图_ideogram4_t2i_2062724777403572226.json, 图片生成/文生图/文生图_ideogram4_t2i_2062789809533448193.json, 图片生成/文生图/文生图_ideogram4_t2i_2070037043585044481.json, 图片生成/文生图/自动版ideogram4生图_2064619048377344001.json, 图片生成/文生图/自动版ideogram4生图_2069077763297996801.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/VividMuse Ideogram4 workflow_2064337095640047618.json、图片生成/文生图/ideogram4-prompt-builder-fixed_2063828351755833345.json、图片生成/文生图/ideogram4_2063180809263206402.json、图片生成/文生图/ideogram4_t2i文生图+Ideogram 4 Prompt Builder KJ_2064175389697724418.json、图片生成/文生图/ideogram4工作流_2062533863087362049.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 25 个 workflow 都包含：
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 24/25 个有
- `PrimitiveStringMultiline` —— 24/25 个有
- `TextGenerate` —— 23/25 个有
- `ConditioningZeroOut` —— 21/25 个有
- `CustomCombo` —— 21/25 个有
- `StringConcatenate` —— 21/25 个有
- `Fast Groups Muter (rgthree)` —— 14/25 个有
- `LoadImage` —— 5/25 个有
- `Ideogram4PromptBuilderKJ` —— 3/25 个有
- `Fast Groups Bypasser (rgthree)` —— 2/25 个有
- `KSampler` —— 2/25 个有
- `ModelSamplingAuraFlow` —— 2/25 个有
- `ShowText|pysssss` —— 2/25 个有
- `AILab_QwenVL` —— 1/25 个有
- `Ideogram4OptimizationsKJ` —— 1/25 个有
- `ImpactSwitch` —— 1/25 个有
- `Seed (rgthree)` —— 1/25 个有
- `easy ifElse` —— 1/25 个有
- `easy promptList` —— 1/25 个有
- `easy showAnything` —— 1/25 个有

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
