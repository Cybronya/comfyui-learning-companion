---
name: unknown_workflow_video_sampler_checkpoint_4
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9075
common_nodes: [ImageOnlyCheckpointLoader, LoadAudio, LoadImage, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/人物照片说话唱歌_音频感知_2085780849454305281.json, 视频生成/图生视频/卡通人物最强对口型Sonic数字人，强烈 推荐！值得一试！_2032256428198600706.json, 视频生成/图生视频/哪吒妈妈唱歌+Ai数字人唱歌=艾橘溪_1891734244585287681.json, 视频生成/图生视频/图生视频-Sonic数字人唱歌对口型_1909784768551055362.json, 视频生成/图生视频/最强对口型Sonic数字人！任意分辨率！艾橘溪_1887696642861367297.json, 音频生成/音频生成/seed-vc 快速语音音色转变+sonic对口型_1928023395433070593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/人物照片说话唱歌_音频感知_2085780849454305281.json、视频生成/图生视频/卡通人物最强对口型Sonic数字人，强烈 推荐！值得一试！_2032256428198600706.json、视频生成/图生视频/哪吒妈妈唱歌+Ai数字人唱歌=艾橘溪_1891734244585287681.json、视频生成/图生视频/图生视频-Sonic数字人唱歌对口型_1909784768551055362.json、视频生成/图生视频/最强对口型Sonic数字人！任意分辨率！艾橘溪_1887696642861367297.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `SaveAudio` —— 3/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `SeedVCNode` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
