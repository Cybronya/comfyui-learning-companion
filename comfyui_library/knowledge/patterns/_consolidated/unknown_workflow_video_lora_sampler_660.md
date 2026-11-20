---
name: unknown_workflow_video_lora_sampler_660
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8995
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy getNode, easy setNode]
problems: []
missing: []
members: [平台全量/Bernini视频编辑-v2.0版本_2071571700168351746.json, 平台全量/Bernini视频编辑-基于Wan2.2视频人物替换动作迁移等_2063291826559344641.json, 平台全量/Bernini视频编辑_2062057725374328833.json, 平台全量/字节跳动开源：Bernini视频编辑-基于Wan2.2_2062335781536100354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_660

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Bernini视频编辑-v2.0版本_2071571700168351746.json、平台全量/Bernini视频编辑-基于Wan2.2视频人物替换动作迁移等_2063291826559344641.json、平台全量/Bernini视频编辑_2062057725374328833.json、平台全量/字节跳动开源：Bernini视频编辑-基于Wan2.2_2062335781536100354.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `BatchImagesNode` —— 2/4 个有
- `BerniniPromptEnhancer` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
