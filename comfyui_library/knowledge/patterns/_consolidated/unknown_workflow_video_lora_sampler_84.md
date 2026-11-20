---
name: unknown_workflow_video_lora_sampler_84
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.948944
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.1图生视频KJ版_1902338359216484353.json, 视频生成/图生视频/WAN2.1街头霸王光波工作流_1894640699545944065.json, 视频生成/图生视频/Wan2.1-胜利之舞_1902955748278571009.json, 视频生成/图生视频/Wan360度旋转-微波炉特效视频工作流_1899781896895881218.json, 视频生成/图生视频/Wan变身超级赛亚人_2079036262153023489.json, 视频生成/图生视频/Wan捏捏图生视频工作流_1899122164795133953.json, 视频生成/图生视频/Wan波动拳图生视频工作流_1899508208174809089.json, 视频生成/图生视频/wan2.1 图生视频-掀起衣服_1900918919576854530.json, 视频生成/图生视频/wan2.1万相图生视拔刀特效lora_1920904820126060546.json, 视频生成/图生视频/wan2.1万相图生视拖红影特效lora_1922514213686886402.json, 视频生成/图生视频/wan2.1图生视频-燃烧特效_1900758531451297794.json, 视频生成/图生视频/wan2.1图生视频特效走秀燃烧起火工作流_1920925508526346241.json, 视频生成/图生视频/wan2.1捏捏乐_1896450417918345217.json, 视频生成/图生视频/【360度旋转】wan2.1人物生成+万物旋转动画视频_1909162790840639489.json, 视频生成/图生视频/双人2对打100wan2.1万相图生视视_1929451203611234306.json, 视频生成/图生视频/街舞单手倒立200确定_1928166272100352001.json, 视频生成/图生视频/街舞大风车176确认好的_1928158479809134593.json, 视频生成/图生视频/通义万相wan2.1万物旋转360度特效_1901238900759609346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/WAN2.1图生视频KJ版_1902338359216484353.json、视频生成/图生视频/WAN2.1街头霸王光波工作流_1894640699545944065.json、视频生成/图生视频/Wan2.1-胜利之舞_1902955748278571009.json、视频生成/图生视频/Wan360度旋转-微波炉特效视频工作流_1899781896895881218.json、视频生成/图生视频/Wan变身超级赛亚人_2079036262153023489.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 18 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTextEncode` —— 17/18 个有
- `WanVideoBlockSwap` —— 16/18 个有
- `WanVideoEnhanceAVideo` —— 14/18 个有
- `ImageResizeKJ` —— 13/18 个有
- `LayerUtility: PurgeVRAM` —— 9/18 个有
- `Int` —— 8/18 个有
- `DownloadAndLoadGIMMVFIModel` —— 6/18 个有
- `GIMMVFI_interpolate` —— 6/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/18 个有
- `Textbox` —— 4/18 个有
- `TextInput_` —— 3/18 个有
- `CR Upscale Image` —— 2/18 个有
- `Note Plus (mtb)` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `VHS_LoadVideo` —— 1/18 个有
- `workflow>文本` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
