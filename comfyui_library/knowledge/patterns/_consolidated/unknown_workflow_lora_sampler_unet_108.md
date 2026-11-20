---
name: unknown_workflow_lora_sampler_unet_108
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.85675
common_nodes: [BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/bernini工作流多图参考生视频，参考图编辑视频_2066150857527357442.json, 平台全量/字节跳动 Bernini ai 视频编辑工作流 - 基于Want2.2架构_2064555014336634881.json, 平台全量/贝尔尼尼Bernini 视频编辑_2062369372651483138.json, 平台全量/贝尔尼尼Bernini 视频编辑加速版_2063915527696896002.json, 数字人/数字人/贝尔尼尼Bernini 视频编辑加速版_2072937099875143681.json, 视频生成/图生视频/贝尔尼尼Bernini 视频编辑加速新版_2061852006909825025.json, 视频生成/图生视频/贝尔尼尼Bernini 视频编辑加速新版_2062526408332763137.json, 视频生成/图生视频/贝尔尼尼Bernini 视频编辑加速新版_2062779488521506817.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_108

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/bernini工作流多图参考生视频，参考图编辑视频_2066150857527357442.json、平台全量/字节跳动 Bernini ai 视频编辑工作流 - 基于Want2.2架构_2064555014336634881.json、平台全量/贝尔尼尼Bernini 视频编辑_2062369372651483138.json、平台全量/贝尔尼尼Bernini 视频编辑加速版_2063915527696896002.json、数字人/数字人/贝尔尼尼Bernini 视频编辑加速版_2072937099875143681.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 7/8 个有
- `BerniniConditioning` —— 7/8 个有
- `CLIPTextEncode` —— 7/8 个有
- `GetVideoComponents` —— 7/8 个有
- `LoadVideo` —— 7/8 个有
- `ImageResizeKJv2` —— 6/8 个有
- `BerniniPromptEnhancer` —— 5/8 个有
- `ImageConcanate` —— 5/8 个有
- `PreviewAny` —— 5/8 个有
- `RHLLMChatNode` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `ImageScaleBy` —— 2/8 个有
- `RIFE VFI` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `BerniniStudio` —— 1/8 个有
- `Int` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `VHS_VideoInfo` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
