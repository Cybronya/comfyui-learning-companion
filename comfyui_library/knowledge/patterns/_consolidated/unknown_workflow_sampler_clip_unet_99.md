---
name: unknown_workflow_sampler_clip_unet_99
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.799333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, JjkText, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, TextCombinerTwo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux文生图(超级简化_带备注)V1.0_1920028263266324482.json, 图片生成/文生图/Flux文生图-1_1_1940662965035233282.json, 图片生成/文生图/Flux文生图_1819583592967110658.json, 图片生成/文生图/Flux文生图_1938488997612027905.json, 图片生成/文生图/Flux文生图_1976282578619637762.json, 图片生成/文生图/Flux文生图（JC自用）_1952547805221064706.json, 平台全量/Flux-3D膨胀膨胀图标元素_1937796235585568770.json, 平台全量/万物青铜_1937074650579111937.json, 平台全量/十二生肖金镶玉摆件_1938524467838517249.json, 平台全量/多彩流动UI图标_1938170290230988801.json, 平台全量/羊毛毡·微观·定格动画_1937078121533198337.json, 平台全量/陶瓷材质盲盒_1937064706081214465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_99

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Flux文生图(超级简化_带备注)V1.0_1920028263266324482.json、图片生成/文生图/Flux文生图-1_1_1940662965035233282.json、图片生成/文生图/Flux文生图_1819583592967110658.json、图片生成/文生图/Flux文生图_1938488997612027905.json、图片生成/文生图/Flux文生图_1976282578619637762.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `JjkText`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 11/12 个有
- `ShowText|pysssss` —— 11/12 个有
- `RH_Translator` —— 9/12 个有
- `PreviewImage` —— 8/12 个有
- `LoraLoader` —— 6/12 个有
- `RH_Prompter` —— 6/12 个有
- `Bjornulf_ShowStringText` —— 3/12 个有
- `CR Text Input Switch (4 way)` —— 3/12 个有
- `ImpactSwitch` —— 3/12 个有
- `CR Text Replace` —— 2/12 个有
- `ArgosTranslateTextNode` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `ShowText` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1280 | 1280 - 1280 | 12 | 100% |
| LoRA 模型强度 | 0.75 | 0.75 - 0.75 | 6 | 100% |
| LoRA 文本强度 | 0.75 | 0.75 - 0.75 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.75，观测区间 0.75 - 0.75，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.75，观测区间 0.75 - 0.75，6 个样本，取值集中（一致性 100%）
