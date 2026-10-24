---
name: unknown_workflow_video_sampler_vae_143
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.75475
common_nodes: [DownloadAndLoadHyVideoTextEncoder, GetImageSizeAndCount, HyVideoBlockSwap, HyVideoDecode, HyVideoEncode, HyVideoEnhanceAVideo, HyVideoGetClosestBucketSize, HyVideoI2VEncode, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoTorchCompileSettings, HyVideoVAELoader, ImageScale, LoadImage, SetNode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/混元视频 I2V 图生视频 Kijai版工作流_1897643797684408322.json, 视频生成/图生视频/混元视频I2V图生视频720PTeaCache加速版_1898316734435414018.json, 视频生成/图生视频/混元视频I2V图生视频janus提示词反推_1903686975529066497.json, 视频生成/图生视频/腾讯混元图生视频K神修复模型人物一致性和稳定性非常好（Rick随风0309更新）_1898690241098633218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_143

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/混元视频 I2V 图生视频 Kijai版工作流_1897643797684408322.json、视频生成/图生视频/混元视频I2V图生视频720PTeaCache加速版_1898316734435414018.json、视频生成/图生视频/混元视频I2V图生视频janus提示词反推_1903686975529066497.json、视频生成/图生视频/腾讯混元图生视频K神修复模型人物一致性和稳定性非常好（Rick随风0309更新）_1898690241098633218.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadHyVideoTextEncoder`
- `GetImageSizeAndCount`
- `HyVideoBlockSwap`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoEnhanceAVideo`
- `HyVideoGetClosestBucketSize`
- `HyVideoI2VEncode`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTeaCache`
- `HyVideoTorchCompileSettings`
- `HyVideoVAELoader`
- `ImageScale`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `Int` —— 2/4 个有
- `JanusImageUnderstanding` —— 1/4 个有
- `JanusModelLoader` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有
- `TextInput_` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
