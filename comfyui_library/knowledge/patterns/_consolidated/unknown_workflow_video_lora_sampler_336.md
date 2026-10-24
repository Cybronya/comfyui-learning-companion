---
name: unknown_workflow_video_lora_sampler_336
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.968833
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2025-5-20-图生视频+修复脸（带反推）_1924496227268743169.json, 视频生成/图生视频/WAN2.1 自定义场景运镜（大师版_1920649191725400066.json, 视频生成/图生视频/【张元英跳舞】WAN2.1 跳舞特效_1914559831519494146.json, 视频生成/图生视频/【视频特效】WAN2.1 人物变身天使_1914500420041961473.json, 视频生成/图生视频/图生视频_1924271202037059586.json, 视频生成/图生视频/让照片说话【万相图生视频】_1914130917185548290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_336

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2025-5-20-图生视频+修复脸（带反推）_1924496227268743169.json、视频生成/图生视频/WAN2.1 自定义场景运镜（大师版_1920649191725400066.json、视频生成/图生视频/【张元英跳舞】WAN2.1 跳舞特效_1914559831519494146.json、视频生成/图生视频/【视频特效】WAN2.1 人物变身天使_1914500420041961473.json、视频生成/图生视频/图生视频_1924271202037059586.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `Int` —— 4/6 个有
- `LayerUtility: PurgeVRAM` —— 3/6 个有
- `WanVideoTeaCache` —— 3/6 个有
- `Fast Bypasser (rgthree)` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 2/6 个有
- `Seed Everywhere` —— 2/6 个有
- `StringConstantMultiline` —— 2/6 个有
- `LayerUtility: TextBox` —— 1/6 个有
- `ReActorFaceSwapOpt` —— 1/6 个有
- `TextBox` —— 1/6 个有
- `Textbox` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
