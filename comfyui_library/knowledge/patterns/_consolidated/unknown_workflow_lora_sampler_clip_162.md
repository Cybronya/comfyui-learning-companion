---
name: unknown_workflow_lora_sampler_clip_162
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8034
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, InFluxModelSamplingPred, LoadImage, LoraLoaderModelOnly, OutFluxModelSamplingPred, PreviewImage, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/CG迷-万物重塑FLUX逆采样工作流_1927290969123610626.json, 平台全量/FLUX电商产品精修，可输入提示词，效果立竿见影_1905053268458786818.json, 平台全量/Fluxtapoz Stylization Kiri Edition_1869930356542443522.json, 平台全量/Flux洗图（皮肤质感偏光滑）_1985947356887691266.json, 平台全量/【阡陌】Fluxtapoz逆采样产品精修工作流_1909475234301227009.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_162

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/CG迷-万物重塑FLUX逆采样工作流_1927290969123610626.json、平台全量/FLUX电商产品精修，可输入提示词，效果立竿见影_1905053268458786818.json、平台全量/Fluxtapoz Stylization Kiri Edition_1869930356542443522.json、平台全量/Flux洗图（皮肤质感偏光滑）_1985947356887691266.json、平台全量/【阡陌】Fluxtapoz逆采样产品精修工作流_1909475234301227009.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `InFluxModelSamplingPred`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageResize+` —— 4/5 个有
- `Image Lucy Sharpen` —— 3/5 个有
- `ViewText` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Florence2ModelLoader` —— 1/5 个有
- `Florence2Run` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `KSampler (Efficient)` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 33 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | sgm_uniform | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
