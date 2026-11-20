---
name: image_to_image_controlnet_ipadapter_lora_7
type: Image To Image
frequency: 2
level: weak
coverage: 0.834
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CR Text, CR Text Concatenate, Canny, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, IPAdapterFaceID, IPAdapterUnifiedLoaderFaceID, KSampler, LoadImage, LoraLoaderModelOnly, OpenposePreprocessor, PreviewImage, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode, WD14Tagger|pysssss, Zoe-DepthMapPreprocessor]
problems: []
missing: []
members: [图片生成/图生图/提示词反推转绘_1900359878983168001.json, 平台全量/CG迷-卡通转绘，Controlnet+FACEID+反推控制转绘_1927257049640423425.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_lora_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/提示词反推转绘_1900359878983168001.json、平台全量/CG迷-卡通转绘，Controlnet+FACEID+反推控制转绘_1927257049640423425.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `Canny`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `IPAdapterFaceID`
- `IPAdapterUnifiedLoaderFaceID`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OpenposePreprocessor`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`
- `Zoe-DepthMapPreprocessor`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.625 | - | 2 | 96% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.525 | - | 2 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.625，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.525，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
