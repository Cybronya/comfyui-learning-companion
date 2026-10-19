---
name: unknown_workflow_sampler_unet_vae_182
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.461
common_nodes: [Anything Everywhere3, CLIPLoader, CR Text, EmptyLatentImage, JjkText, KSampler, LoadImage, PrimitiveInt, PrimitiveStringMultiline, QwenImage21Cache, RegexExtract, ResolutionSelector, SaveImage, Seed (rgthree), TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, YuanMultiImage, easy batchAnything, easy forLoopEnd, easy forLoopStart, sch_split_text, 孤海注释]
problems: []
missing: []
members: [图片生成/反推提示词/短剧拍档支持场景和角色V11.5(千问qwen image 2.1)一键生成全部资产人物+道具+场景_2103731317375594497.json, 图片生成/文生图/短剧拍档支持场景和角色V11.5(千问qwen image 2.1)一键生成全部资产人物+道具+场景_2103731317375594497.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_182

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/短剧拍档支持场景和角色V11.5(千问qwen image 2.1)一键生成全部资产人物+道具+场景_2103731317375594497.json、图片生成/文生图/短剧拍档支持场景和角色V11.5(千问qwen image 2.1)一键生成全部资产人物+道具+场景_2103731317375594497.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CR Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `RegexExtract`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`
- `YuanMultiImage`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `sch_split_text`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 40 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
