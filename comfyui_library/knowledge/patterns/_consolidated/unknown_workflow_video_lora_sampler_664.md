---
name: unknown_workflow_video_lora_sampler_664
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.966333
common_nodes: [LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/视频一句话转画风_1980290599200972802.json, 数字人/数字人/视频风格 一键转绘 高效 极简 Ditto_1980279788386607106.json, 视频生成/图生视频/ditto视频风格转绘工作流_1980897835057106945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_664

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/视频一句话转画风_1980290599200972802.json、数字人/数字人/视频风格 一键转绘 高效 极简 Ditto_1980279788386607106.json、视频生成/图生视频/ditto视频风格转绘工作流_1980897835057106945.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `TextInputBasic` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Note _O` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `VHS_VideoInfoLoaded` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
