---
name: unknown_workflow_video_sampler_clip_20
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.950842
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/扭扭弹弹跳舞_1904411310740905985.json, 图片生成/文生图/2025重磅更新WANX2.1模型，内含图生视频！文生视频，高清720p_1896112344349474817.json, 平台全量/wan2.1 360旋特效_1901198215566499842.json, 视频生成/图生视频/Wan视频-召唤法相2.0_1913798137197330434.json, 视频生成/图生视频/wan2.1图生视频，更新快速节点_1896816638631550978.json, 视频生成/图生视频/wan图生视频+超高清补帧_1903839569089826817.json, 视频生成/图生视频/一键泄气特效-万相wan2.1新玩意_1899415692570181634.json, 视频生成/图生视频/万物被捏扁特效-万相wan2.1新玩意_1899312280767516673.json, 视频生成/图生视频/万相WAN2.1，美女一键跳舞！_1910726225436864514.json, 视频生成/图生视频/万相WAN2.1，美女一键跳舞！_1911140460969062401.json, 视频生成/图生视频/冲锋枪射击特效-万相wan2.1新玩意_1899671568367177729.json, 视频生成/图生视频/女子搏击，香香的粉拳-万相wan2.1_1900467836874301442.json, 视频生成/图生视频/新版360度旋转特效-万相wan_1899699069881860097.json, 视频生成/图生视频/新版360度旋转特效-万相wan_2005178859836370946.json, 视频生成/图生视频/特效合集，wan2.1图生视频，加速高清版_1899713009114107905.json, 视频生成/图生视频/🦖wan2.1图生视频(更新至0325)高清修复+lora修复_1894935249389039617.json, 视频生成/图生视频/🦖大风车转呀转_1932255495774437378.json, 视频生成/图生视频/🦖浪花特效_1930816773925306370.json, 视频生成/文生视频/wan图生视频+超高清补帧_1904728293755813889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/扭扭弹弹跳舞_1904411310740905985.json、图片生成/文生图/2025重磅更新WANX2.1模型，内含图生视频！文生视频，高清720p_1896112344349474817.json、平台全量/wan2.1 360旋特效_1901198215566499842.json、视频生成/图生视频/Wan视频-召唤法相2.0_1913798137197330434.json、视频生成/图生视频/wan2.1图生视频，更新快速节点_1896816638631550978.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 19 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 18/19 个有
- `ImageUpscaleWithModel` —— 15/19 个有
- `LayerUtility: PurgeVRAM` —— 15/19 个有
- `UpscaleModelLoader` —— 15/19 个有
- `WanVideoEnhanceAVideo` —— 15/19 个有
- `WanVideoTeaCache` —— 15/19 个有
- `WanVideoTorchCompileSettings` —— 12/19 个有
- `Int` —— 9/19 个有
- `Note Plus (mtb)` —— 7/19 个有
- `RIFE VFI` —— 7/19 个有
- `ImageResizeAdvanced` —— 5/19 个有
- `Fast Groups Bypasser (rgthree)` —— 3/19 个有
- `TextInput_` —— 3/19 个有
- `WanVideoEmptyEmbeds` —— 3/19 个有
- `Text Multiline` —— 2/19 个有
- `WanVideoSLG` —— 2/19 个有
- `ImageResizeKJ` —— 1/19 个有
- `ResizeLongestToNode` —— 1/19 个有
- `SaveLatent` —— 1/19 个有
- `Simple String` —— 1/19 个有
- `easy cleanGpuUsed` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
